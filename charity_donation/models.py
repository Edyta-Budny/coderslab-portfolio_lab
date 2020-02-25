from django.db import models

TYPES = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(max_length=64, choices=TYPES, default=1)
    categories = models.ManyToManyField("Category")


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField("Category")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.TextField()
