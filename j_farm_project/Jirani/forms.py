from django import forms
from django.contrib.auth.models import User
from .models import Farmer, Tractor, Lease


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['phone', 'location']


class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractor
        fields = ['model', 'year', 'price', 'available']


class LeaseForm(forms.ModelForm):
    class Meta:
        model = Lease
        fields = ['start_date', 'end_date']
