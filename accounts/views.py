from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import RedirectView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from accounts.forms import SignUpForm


# Create your views here.


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('tasks:task_list')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks:task_list')

    def get_success_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')