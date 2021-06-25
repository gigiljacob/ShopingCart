from django.urls import path

from . import views as shop_view

app_name = 'shop'

urlpatterns = [
    path('', shop_view.Home.as_view(), name='home'),
    path('product/', shop_view.ProductList.as_view(), name='products'),
    path('product/<slug:slug>', shop_view.ProductView.as_view(), name='review'),
]