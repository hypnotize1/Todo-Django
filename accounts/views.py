from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from accounts.forms import CustomSignUpForm, CustomLoginForm


# Create your views here.


class SignUpView(CreateView):
    model = User
    form_class = CustomSignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('tasks:task_list')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    authentication_form = CustomLoginForm
    success_url = reverse_lazy('tasks:task_list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


class CustomPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'

class CustomPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class CustomPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')

class CustomPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
