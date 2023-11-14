from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
UserCreationForm as UserCreationFormDjango
)


from django import forms
from django.utils.translation import  gettext_lazy as _

User = get_user_model()

class AuthenticationHomeetForm(forms.Form):
    #username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email'})
    )

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

class UserCreationForm(UserCreationFormDjango):
    email = forms.EmailField(
        label=("Email"),
        max_length = 254,
        widget = forms.EmailInput (attrs={'autocomplete': 'email'})
    )
    class Meta(UserCreationFormDjango.Meta):
        model = User
        fields = ("username", "email")
