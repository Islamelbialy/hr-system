from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import signUpForm
# Create your views here.

class signUpView(CreateView):
    form_class = signUpForm
    template_name = 'accounts\signUp.html'
    success_url = reverse_lazy('branches')
    