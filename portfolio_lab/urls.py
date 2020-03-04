from django.contrib import admin
from django.urls import path

from auth_user.views import LoginView, LogoutView, RegisterView
from charity_donation.views import AddDonationView, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="main"),
    path('add_donation/', AddDonationView.as_view(), name="donation"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
