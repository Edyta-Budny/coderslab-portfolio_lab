from django import forms
# from charity_donation.models import
from django.core.exceptions import ValidationError

from auth_user.models import User


def ThisEmailAlreadyExistsValidator(value):
    emails = User.objects.all().filter(email=value)
    if emails:
        raise ValidationError("Ten email już istanieje.")


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Imię'}), label=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}), label=False)
    email = forms.EmailField(validators=[ThisEmailAlreadyExistsValidator],
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}), label=False)
    repeated_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Hasło powtórzone'}),
                                        label=False)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_repeated = cleaned_data.get('repeated_password')
        if password != password_repeated:
            raise forms.ValidationError("Sprobuj ponownie wpisac haslo!")
