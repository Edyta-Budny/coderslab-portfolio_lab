from django import forms
from django.utils.translation import ugettext_lazy as _


class DonationForm(forms.Form):
    quantity = forms.IntegerField(label=_('Number of 60 liter bags'))
    address = forms.CharField(max_length=128, label=_('Address'))
    city = forms.CharField(max_length=128, label=_('City'))
    zip_code = forms.CharField(label=_('Postcode'))
    phone_number = forms.CharField(max_length=9, label=_('Phone number'))
    pick_up_date = forms.DateField(label=_('Data'), widget=forms.DateInput(attrs={'placeholder': 'RRRR-MM-DD'}))
    pick_up_time = forms.TimeField(label=_('Time'), widget=forms.TimeInput(attrs={'placeholder': '--:--'}))
    pick_up_comment = forms.CharField(label=_('Comment'), widget=forms.Textarea(attrs={'rows': '5'}), required=False)

