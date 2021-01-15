from django.db import models
from django.contrib.auth.models import User


PRACTICIONER_CHOICES = (
    ('-','-'),
    ('RESIDENT','RESIDENT'),
    ('SENIOR-RESIDENT','SENIOR-RESIDENT'),
    ('ASSISTANT','ASSISTANT'),
    ('CONSULTANT','CONSULTANT'),
    ('OTHER','OTHER'),
)

SPECIALIAZES_IN = (
    ('-','-'),
    ('NEUROLOGY','NEUROLOGY'),
    ('CRANIOTOMY','CRANIOTOMY'),
    ('OPTAMOLOGY','OPTAMOLOGY'),
    ('GYNAECOLOGY','GYNAECOLOGY'),
    ('UROLOGY','UROLOGY'),
    ('OTHER','OTHER')
)


DISEASES = (
    ('NONE','NONE'),
    ('ARTHRITIS','ARTHRITIS'),
    ('ANAEMIA','ANAEMIA'),
    ('ASTHMA','ASTHMA'),
    ('STD','STD'),
    ('HEART FAILURE','HEART FAILURE'),
    ('EPILEPSY','EPILEPSY'),
    ('DIABETES','DIABETES'),
    ('OTHER','OTHER'),
)

GENDERS = (
    ('M','M'),
    ('F','F')
    )

EPIDEMICS = (
    ('NONE','NONE'),
    ('HIV','HIV'),
    ('EBOLA','EBOLA'),
    ('COVID-19','COVID-19')
)

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(default='profiles/avatar.png',upload_to='profiles')
    field = models.CharField(choices = SPECIALIAZES_IN,max_length = 100,blank=True,null=True)
    level = models.CharField(choices = PRACTICIONER_CHOICES, max_length=100,blank=True,null=True)
    is_practicioner = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.get_full_name()



class MedicalDetails(models.Model):
    profile = models.OneToOneField(Profile,related_name='medical_form',on_delete=models.SET_NULL,null=True,blank=True)
    gender = models.CharField(choices=GENDERS,max_length=2)
    under_medical_treatment = models.BooleanField(default=False)
    hospitalized_within_5_years = models.BooleanField(default=False)
    on_special_diet = models.BooleanField(default=False)
    diseased = models.CharField(choices = DISEASES,max_length=100)
    other_disease = models.CharField(max_length=100,null=True,blank=True)
    allergies= models.CharField(max_length=1000,null=True,blank=True)
    # pregnant = models.BooleanField(default=False)
    had_any_recent_disease = models.CharField(choices=EPIDEMICS,max_length=100)



    
    