from django.shortcuts import render
from django.views import View
from charity_donation.models import Donation


class LandingPageView(View):
    def get(self, request):
        sack_counter = 0
        supported_institution = []
        supported_institution_counter = 0
        donations = Donation.objects.all()
        for donation in donations:
            sack_counter += donation.quantity
            if donation.institution.name not in supported_institution:
                supported_institution.append(donation.institution.name)
                supported_institution_counter += len(supported_institution)
        return render(request, "html/index.html", {"sack_counter": sack_counter,
                                                   "supported_institution_counter": supported_institution_counter})


class AddDonationView(View):
    def get(self, request):
        return render(request, "html/form.html")


class LoginView(View):
    def get(self, request):
        return render(request, "html/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "html/register.html")
