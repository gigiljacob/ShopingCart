from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView

from .models import SellerInformation


class Profile(UpdateView):
    template_name = 'company/profile.html'
    model = SellerInformation


class Dashboard(TemplateView):
    template_name = 'company/dashboard.html'

