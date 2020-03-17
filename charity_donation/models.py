from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


class Institution(models.Model):
    FOUNDATION = "F"
    NONGOVERNMENTAL_ORGANIZATION = "NO"
    LOCAL_COLLECTION = "LC"
    TYPES = (
        (FOUNDATION, _('foundation')),
        (NONGOVERNMENTAL_ORGANIZATION, _('nongovernmental organization')),
        (LOCAL_COLLECTION, _('local collection')),
    )
    name = models.CharField(max_length=64, verbose_name=_('name'))
    description = models.TextField(verbose_name=_('description'))
    type = models.CharField(max_length=64, choices=TYPES, default=FOUNDATION, verbose_name=_('type'))
    categories = models.ManyToManyField("Category", verbose_name=_('categories'))

    class Meta:
        verbose_name = _('institution')
        verbose_name_plural = _('institutions')

    def __str__(self):
        return self.name


class Donation(models.Model):
    quantity = models.IntegerField(verbose_name=_('quantity'))
    categories = models.ManyToManyField("Category", verbose_name=_('categories'))
    institution = models.ForeignKey("Institution", on_delete=models.CASCADE, verbose_name=_('institution'))
    address = models.CharField(max_length=120, verbose_name=_('address'))
    phone_number = models.IntegerField(verbose_name=_('phone number'))
    city = models.CharField(max_length=120, verbose_name=_('city'))
    zip_code = models.CharField(max_length=6, verbose_name=_('zip code'))
    pick_up_date = models.DateField(verbose_name=_('pick up date'))
    pick_up_time = models.TimeField(verbose_name=_('pick up time'))
    pick_up_comment = models.TextField(verbose_name=_('pick up comment'))
    is_taken = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        default=None,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=_('user')
    )

    class Meta:
        verbose_name = _('donation')
        verbose_name_plural = _('donations')

    def __str__(self):
        return _('Donation for') + f' {self.institution}'

