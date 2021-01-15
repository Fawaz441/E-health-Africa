from django import forms
from .models import (MedicalDetails,PRACTICIONER_CHOICES,
                     SPECIALIAZES_IN,DISEASES,EPIDEMICS,GENDERS)



class UserSignupForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'au-input au-input--full','placeholder':'Email'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'au-input au-input--full','placeholder':'First Name'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'au-input au-input--full','placeholder':'Last Name'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder':'Password'}))
    confirm_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder':'Confirm Password'}))
    # is_medical_practicioner = forms.BooleanField(widget=forms.CheckboxInput())
    
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
            raise forms.ValidationError('The passwords do not match!')
        
        
class PracticionerSignupForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'au-input au-input--full','placeholder':'Email'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'au-input au-input--full','placeholder':'First Name'}))
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'au-input au-input--full','placeholder':'Last Name'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder':'Password'}))
    confirm_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'au-input au-input--full','placeholder':'Confirm Password'}))
    level = forms.ChoiceField(choices=PRACTICIONER_CHOICES,required=True,widget=forms.Select(attrs={'class':'au-input au-input--full spread'}))
    field = forms.ChoiceField(choices=SPECIALIAZES_IN,required=True,widget=forms.Select(attrs={'class':'au-input au-input--full spread'}))
    
    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('confirm_password'):
            raise forms.ValidationError('The passwords do not match!')
        if self.cleaned_data.get('field') == '-':
            raise forms.ValidationError('Inappropriate field selected')
        if self.cleaned_data.get('level') == '-':
            raise forms.ValidationError('Invalid level selected')
        
        
class MedicalForm(forms.ModelForm):
    class Meta:
        model = MedicalDetails
        fields = [
            'gender',
            'under_medical_treatment',
            'hospitalized_within_5_years',
            'on_special_diet',
            'diseased',
            'other_disease',
            'allergies',
            # 'pregnant',
            'had_any_recent_disease'
            ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['gender']=forms.ChoiceField(choices=GENDERS,required=True,widget=forms.Select(attrs={'class':'form-control'}))
        self.fields['diseased']=forms.ChoiceField(choices=DISEASES,required=True,widget=forms.Select(attrs={'class':'form-control'}))
        self.fields['had_any_recent_disease']=forms.ChoiceField(choices=EPIDEMICS,required=True,widget=forms.Select(attrs={'class':'form-control'}))
        self.fields['allergies'] = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
        self.fields['other_disease'] = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)