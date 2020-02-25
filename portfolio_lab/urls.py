from django.contrib import admin
from django.urls import path

from charity_donation.views import LandingPageView, AddDonationView, LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view()),
    path('add_donation/', AddDonationView.as_view()),
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
]

