from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('userapp:home')  # 성공시 연결 url
    template_name = 'userapp/create.html'

