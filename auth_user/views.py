from django.shortcuts import render, redirect
from django.views import View
from auth_user.forms import RegisterForm
from auth_user.models import User


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "html/register.html", {"form": form})

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
            return render(request, "html/register.html", {"form": form})
