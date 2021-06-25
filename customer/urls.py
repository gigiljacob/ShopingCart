from django.urls import path

from . import views as customer_view

app_name='customer'


urlpatterns = [
    path('orderHistory/', customer_view.OrderHistory.as_view(), name='order_history'),
]