from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from auth_user.models import User


def ThisEmailAlreadyExistsValidator(value):
    emails = User.objects.filter(email=value)
    if emails:
        raise ValidationError(_('Email or password is not available.'))


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('First name')}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': _('Last name')}))
    email = forms.EmailField(
        validators=[ThisEmailAlreadyExistsValidator],
        widget=forms.EmailInput(attrs={'placeholder': _('Email')})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Password')}))
    confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Confirmation')}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmation_password = cleaned_data.get('confirmation')
        if password != confirmation_password:
            raise forms.ValidationError(_("Try entering the password again."))


class LoginForm(forms.Form):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Email')}), label=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Password')}), label=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(_("The email or password you entered isn't correct. Try entering it again."))
