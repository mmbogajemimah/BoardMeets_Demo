from django import forms
from .models import Organization, Leader

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class LeaderForm(forms.ModelForm):
    class Meta:
        model = Leader
        fields = ['name', 'title', 'email', 'contact']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['phone_number']