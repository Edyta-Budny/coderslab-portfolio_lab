from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Institution(models.Model):
    FOUNDATION = "F"
    NONGOVERNMENTAL_ORGANIZATION = "NO"
    LOCAL_COLLECTION = "LC"
    TYPES = (
        (FOUNDATION, "fundacja"),
        (NONGOVERNMENTAL_ORGANIZATION, "organizacja pozarządowa"),
        (LOCAL_COLLECTION, "zbiórka lokalna"),
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=64, choices=TYPES, default=FOUNDATION)
    categories = models.ManyToManyField("Category")

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField("Category")
    institution = models.ForeignKey("Institution", on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, blank=True, on_delete=models.CASCADE)
