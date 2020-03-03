from django.shortcuts import render
from django.views import View
from charity_donation.models import Donation, Institution
from django.db.models import Count, Sum


class LandingPageView(View):
    def get(self, request):
        sack_counter = Donation.objects.aggregate(sum_q=Sum('quantity'))["sum_q"]
        supported_institution = Institution.objects.annotate(count_d=Count('donation')).filter(count_d__gte=1).count()
        # supported_institution = Institution.objects.aggregate(count_q=Count('name'))["count_q"]
        foundation_list = Institution.objects.filter(type="F")
        organization_list = Institution.objects.filter(type="NO")
        collection_list = Institution.objects.filter(type="LC")
        return render(request, "html/index.html", {"sack_counter": sack_counter,
                                                   "supported_institution_counter": supported_institution,
                                                   "foundations": foundation_list,
                                                   "organizations": organization_list,
                                                   "collections": collection_list})


class AddDonationView(View):
    def get(self, request):
        return render(request, "html/form.html")

