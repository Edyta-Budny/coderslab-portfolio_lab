from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from auth_user.views import LoginView, LogoutView, RegisterView
from charity_donation.views import AddDonationView, LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="main"),
    path('add_donation/', AddDonationView.as_view(), name="donation"),
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
