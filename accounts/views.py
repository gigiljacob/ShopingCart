from django.contrib.auth import authenticate, views as auth_view
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, FormView

from accounts.forms import SignUpForm
from shoping_cart.local_settings import COMPANY_NAME


class Profile(TemplateView):
    template_name = 'your_accounts.html'
    

class Security(TemplateView):
    template_name = 'security.html'


class Prime(TemplateView):
    template_name = 'prime.html'


class Register(CreateView):
    """
    Register a new customer
    """
    form_class = SignUpForm
    template_name = 'register.html'

    def form_valid(self, form):
        view = super(Register, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        print(username, password)
        user = authenticate(username=username, password=password)
        return view

    def get_success_url(self):
        return reverse('shop:home')


class SignIn(auth_view.LoginView, FormView):
    """
    Allow already existing customer to sign in
    """
    template_name = 'signin.html'

    def get_context_data(self, **kwargs):
        context = super(SignIn, self).get_context_data()
        context['company_name'] = COMPANY_NAME
        return context

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse('company:company_profile')
        else:
            return reverse('shop:home')


class SignOut(auth_view.LogoutView):

    def get_success_url_allowed_hosts(self):
        return reverse('accounts:signin')
