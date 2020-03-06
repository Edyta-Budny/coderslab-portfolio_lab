from django.db.models import Count, Sum
from django.shortcuts import render
from django.views import View

from charity_donation.models import Donation, Institution


class LandingPageView(View):
    def get(self, request):
        sack_counter = Donation.objects.aggregate(sum_q=Sum('quantity'))["sum_q"]
        supported_institution = Institution.objects.annotate(count_d=Count('donation')).filter(count_d__gte=1).count()
        foundation_list = Institution.objects.filter(type=Institution.FOUNDATION)
        organization_list = Institution.objects.filter(type=Institution.NONGOVERNMENTAL_ORGANIZATION)
        collection_list = Institution.objects.filter(type=Institution.LOCAL_COLLECTION)
        return render(
            request,
            "html/index.html",
            {
                "sack_counter": sack_counter,
                "supported_institution_counter": supported_institution,
                "foundations": foundation_list,
                "organizations": organization_list,
                "collections": collection_list
            }
        )


class AddDonationView(View):
    def get(self, request):
        return render(request, "html/form.html")