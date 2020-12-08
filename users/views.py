from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from .models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)

    else:
        form = LoginForm()

    return render(request, "users/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("users:login")


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            nick_name = form.cleaned_data['nick_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            profile_img = form.cleaned_data['profile_img']

            user = User.objects.create_user(email, password, nick_name, date_of_birth, profile_img)

            return redirect("users:login")

    else:
        form = SignupForm()

    return render(request, "users/signup.html", {'form': form})


# 추가 - 회원정보
class mypage_view():
    template_name = "users/mypage.html"
