from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth import logout as django_logout


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from userapp.forms import SignupForm, LoginForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('userapp:login')
    else:
        form = SignupForm()
    return render(request, 'userapp/signup.html', {'form': form} )

def login_check(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        name = request.POST.get('username')
        pwd = request.POST.get('password')

        user = authenticate(username=name, password=pwd)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "userapp/login_fail_info.html")
    else:
        form = LoginForm()
        return render(request, 'userapp/login.html', {"form":form})

def logout(request):
    django_logout(request)
    return redirect('/')


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('userapp:home')  # 성공시 연결 url
    template_name = 'userapp/create.html'
