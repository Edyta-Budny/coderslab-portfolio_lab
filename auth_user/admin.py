from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from auth_user.models import User
from charity_donation.models import Institution, Donation, Category

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Institution)
admin.site.register(Donation)
