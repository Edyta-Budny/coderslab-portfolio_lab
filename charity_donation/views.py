from django.shortcuts import render
from django.views import View


class LandingPageView(View):
    def get(self, request):
        return render(request, "html/index.html")


class AddDonationView(View):
    def get(self, request):
        return render(request, "html/form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "html/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "html/register.html")
