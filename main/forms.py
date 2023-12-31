from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserWithKey

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    request_manager = forms.BooleanField(label='Request Manager Status', required=False)

    class Meta:
        model = UserWithKey
        fields = ["username", "email", "password1", "password2", "first_name", "last_name", "address", "phone_number"]


class UpdateProfileForm(UserChangeForm):
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = UserWithKey
        fields = ['first_name', 'last_name', 'email', 'address', 'phone_number']