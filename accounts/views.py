from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from .models import Profile,MedicalDetails
from .forms import UserSignupForm,PracticionerSignupForm,MedicalForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny

def get_data(user):
    name =  user.get_full_name()
    image = user.profile.image.url
    email = user.email
    is_practicioner = user.profile.is_practicioner
    return {'name':name,'image':image,'email':email,'is_practicioner':is_practicioner}


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')
            new_user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=email,
                )
            new_user.set_password(password)
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            login(request,new_user)
            request.session['userdetails'] = get_data(new_user)
            return redirect('home')
    return render(request,'accounts/signup.html',{'form':form})
        
        
        
def practicioner_signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = PracticionerSignupForm()
    if request.method == 'POST':
        form = PracticionerSignupForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')
            field = cleaned_data.get('field')
            level = cleaned_data.get('level')
            new_user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=email,
                )
            new_user.set_password(password)
            new_user.save()
            profile = Profile.objects.create(
                user=new_user,
                is_practicioner=True,
                level=level,
                field=field
                )
            login(request,new_user)
            request.session['userdetails'] = get_data(new_user)
            return redirect('home')
    return render(request,'accounts/prac_signup.html',{'form':form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
        else:
            messages.error(request,'Incorrect credentials')
            return redirect('home')
        request.session['userdetails'] = get_data(user)
        return redirect('home')
    return render(request,'accounts/login.html')
    

class Home(LoginRequiredMixin,TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        if MedicalDetails.objects.filter(profile = user.profile).exists():
            context['has_form'] = True
        context.update(self.request.session['userdetails'])
        return context
        

def logout_view(request):
    if request.session.has_key('userdetails'):
        del request.session['userdetails']
    logout(request)
    return redirect('login')



class MedicalInfoCreate(LoginRequiredMixin,CreateView):
    template_name = 'medical/medical_info.html'
    form_class = MedicalForm

    def form_valid(self,form):
        user_profile = self.request.user.profile
        form = form.save(commit=False)
        form.profile = user_profile
        form.save()
        messages.info(self.request,'Form completed successfully')
        return redirect('home')

    def form_invalid(self,form):
        messages.error(self.request,"There was an error. Try filling the form again")
        return redirect('medical_info_create')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['has_form'] = False
        context.update(self.request.session['userdetails'])
        return context

class MedicalInfoUpdate(LoginRequiredMixin,UpdateView):
    template_name = 'medical/medical_info.html'
    form_class = MedicalForm

    def get_object(self):
        profile = self.request.user.profile
        return MedicalDetails.objects.get(profile=profile)

    def form_valid(self,form):
        form.save()
        return redirect('home')

    def form_invalid(self,form):
        messages.error(self.request,"There was an error. Try filling the form again")
        return redirect('medical_info_update')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['has_form'] = True
        context.update(self.request.session['userdetails'])
        return context
        

class InfectionCountView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        cases = MedicalDetails.objects.all()
        hiv_count = cases.filter(had_any_recent_disease = 'HIV').count()
        ebola_count = cases.filter(had_any_recent_disease = 'EBOLA').count()
        covid_count = cases.filter(had_any_recent_disease = 'COVID-19').count()
        return Response({'counts':[ebola_count,hiv_count,covid_count]},status=HTTP_200_OK)


class DiseasesCountView(APIView):
    permission_classes = (AllowAny,)
    def get(self,request):
        diseases = {}
        # not using postgres
        cases = list(set(MedicalDetails.objects.values_list('diseased')))
        for case in cases:
            t = case[0]
            diseases[t] = MedicalDetails.objects.filter(diseased=t).count()
        return Response(diseases,status=HTTP_200_OK)



def filteruser(request):
    if not request.user.profile.is_practicioner:
        messages.error(request,'You are not authorized to view this page!')
        return redirect('home')
    medical_records = MedicalDetails.objects.all()
    context = {
        'medical_records':medical_records,
        'conditions':[
                'NONE',
                'ARTHRITIS',
                'ANAEMIA',
                'ASTHMA',
                'STD',
                'HEART FAILURE',
                'EPILEPSY',
                'DIABETES',
                'OTHER'    
                ],
        'has_form':True
    }
    context.update(request.session['userdetails'])
    return render(request,'medical/filter_users.html',context)


            