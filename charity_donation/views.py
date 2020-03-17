from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum
from django.shortcuts import render, redirect
from django.views import View

from charity_donation.forms import DonationForm
from charity_donation.models import Category, Donation, Institution


class LandingPageView(View):
    def get(self, request):
        sack_counter = Donation.objects.aggregate(sum_q=Sum('quantity'))["sum_q"]
        supported_institution = Institution.objects.annotate(count_d=Count('donation')).filter(count_d__gte=1).count()
        foundation_list = Institution.objects.filter(type=Institution.FOUNDATION)
        organization_list = Institution.objects.filter(type=Institution.NONGOVERNMENTAL_ORGANIZATION)
        collection_list = Institution.objects.filter(type=Institution.LOCAL_COLLECTION)
        return render(
            request,
            "base.html",
            {
                "sack_counter": sack_counter,
                "supported_institution_counter": supported_institution,
                "foundations": foundation_list,
                "organizations": organization_list,
                "collections": collection_list
            }
        )


class AddDonationView(LoginRequiredMixin, View):
    def get(self, request):
        form = DonationForm()
        categories = Category.objects.all().order_by('id')
        institutions = Institution.objects.all()
        return render(
            request,
            "form.html",
            {
                "form": form,
                "categories": categories,
                "institutions": institutions,
            }
        )

    def post(self, request):
        quantity = request.POST["quantity"]
        address = request.POST["address"]
        phone_number = request.POST["phone_number"]
        city = request.POST["city"]
        zip_code = request.POST["zip_code"]
        pick_up_date = request.POST["pick_up_date"]
        pick_up_time = request.POST["pick_up_time"]
        pick_up_comment = request.POST["pick_up_comment"]
        institution = request.POST["institution_id"]
        categories_get = tuple(map(int, (request.POST.get("categories_id"))))
        user = request.user.id
        donation = Donation.objects.create(quantity=quantity, address=address, phone_number=phone_number,
                                           city=city, zip_code=zip_code, pick_up_date=pick_up_date,
                                           pick_up_time=pick_up_time, pick_up_comment=pick_up_comment,
                                           institution_id=institution, user_id=user)
        for category in categories_get:
            donation.categories.add(category)
        return render(request, "form-confirmation.html")


class ConfirmationView(View):
    def get(self, request):
        return render(request, "form-confirmation.html")
