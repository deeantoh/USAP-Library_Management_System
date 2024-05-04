from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy # Login required to access private pagas
from django.views.decorators.cache import cache_control
from Accounts.forms import SignUpForm
from django.views.generic import TemplateView, CreateView, View


# Frontend
def frontend(request):
    return render(request, "auth/frontend.html")

# Backend
@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "auth/backend.html")

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
