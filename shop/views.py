from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ProductCategory, Product


class ProductList(TemplateView):
    template_name = 'products.html'


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        context['products'] = Product.objects.all()
        return context


class ProductView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_view.html'

    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context['page'] = 'product_view'
         return context
