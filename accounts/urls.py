from django.urls import path
from django.contrib.auth import views as auth_view

from accounts import views as accounts_view

app_name = 'accounts'

urlpatterns = [
    path('', accounts_view.Profile.as_view(), name='profile'),
    path('security/', accounts_view.Security.as_view(), name='security'),
    path('prime/', accounts_view.Prime.as_view(), name='prime'),

    path('register/', accounts_view.Register.as_view(), name='register'),
    path('login/', accounts_view.SignIn.as_view(), name='signin'),
    path('sign_out/', accounts_view.SignOut.as_view(), name='sign_out')
]
