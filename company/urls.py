from django.urls import path

from . import views as company_view

app_name = 'company'

urlpatterns = [
    path('profile/', company_view.Profile.as_view(), name='company_profile'),
    path('dashboard/', company_view.Dashboard.as_view(), name='dashboard'),
]