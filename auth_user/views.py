from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views import View

from auth_user.forms import LoginForm, RegisterForm
from auth_user.models import User


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            return redirect("login")
        else:
            return render(request, "register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                return redirect("register")
        else:
            return render(request, "login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("main")


class MainPageUserView(View):
    def get(self, request):
        return render(request, "profile.html")