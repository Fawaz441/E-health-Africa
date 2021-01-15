from django.urls import path
from .views import (signup,Home,practicioner_signup,
                    login_view,logout_view,
                    MedicalInfoCreate,MedicalInfoUpdate,
                    InfectionCountView,DiseasesCountView,
                    filteruser)

urlpatterns = [
    path('signup/practicioner',practicioner_signup,name='prac_signup'),
    path('signup',signup,name='signup'),
    path('',Home.as_view(),name='home'),
    path('logout',logout_view,name='logout'),
    path('login',login_view,name='login'),
    path('medical-info-create',MedicalInfoCreate.as_view(),name='medical_info_create'),
    path('medical-info-update/<pk>',MedicalInfoUpdate.as_view(),name='medical_info_update'),
    path('chart-data',InfectionCountView.as_view(),name='chart_data'),
    path('diseases-data',DiseasesCountView.as_view(),name='diseases_data'),
    path('filter-users',filteruser,name='filter_users'),
]