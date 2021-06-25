from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class OrderHistory(LoginRequiredMixin, TemplateView):
    template_name = 'order_history.html'
