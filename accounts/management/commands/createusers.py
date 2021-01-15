import random
import names
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile, MedicalDetails

booleans = [True,False]
specializes = [ 'NEUROLOGY', 'CRANIOTOMY', 'OPTAMOLOGY', 'GYNAECOLOGY', 'UROLOGY', 'OTHER', ]
diseases = [ 'NONE', 'ARTHRITIS', 'ANAEMIA', 'ASTHMA', 'STD', 'HEART FAILURE', 'EPILEPSY', 'DIABETES', 'OTHER' ]
genders = ['M','F']
levels = [ 'RESIDENT', 'SENIOR-RESIDENT', 'ASSISTANT', 'CONSULTANT', 'OTHER', ]
epidemics = [ 'NONE', 'HIV', 'EBOLA', 'COVID-19', ]
full_gender = ['male','female']



class Command(BaseCommand):
    def handle(self, *args, **options):
        for x in range(100):
            gender = random.choice(full_gender)
            first_name = names.get_first_name(gender=gender)
            last_name = names.get_last_name()
            email = first_name+random.choice(['@yahoo.com','@gmail.com'])
            user = User(
                username=email+str(x),
                first_name=first_name,
                last_name=last_name
                )
            user.set_password(random.choice(full_gender))
            user.save()
            is_practicioner = random.choice(booleans)
            if is_practicioner:
                profile = Profile(user=user,
                field=random.choice(specializes),
                level = random.choice(levels),
                is_practicioner = True
                )
                profile.save()
            else:
                profile = Profile(user=user,
                field=random.choice(specializes),
                level = random.choice(levels),
                )
                profile.save()
                if(gender=='male'):
                    gi = 'M'
                else:
                    gi = 'F'
                MedicalDetails.objects.create(
                    profile = profile,
                    gender = gi,
                    under_medical_treatment = random.choice(booleans),
                    hospitalized_within_5_years = random.choice(booleans),
                    on_special_diet = random.choice(booleans),
                    diseased = random.choice(diseases),
                    other_disease = 'No',
                    allergies = random.choice(['No','Eggs','Smoke','Fish']),
                    had_any_recent_disease = random.choice(epidemics)
                )
           
