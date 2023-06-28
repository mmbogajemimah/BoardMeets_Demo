from django import forms
from .models import Organization, Leader, License

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

class SocialForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['social_media_facebook', 'social_media_instagram', 'social_media_linkedin', 'social_media_twitter']

class LicenseForm(forms.ModelForm):
    class Meta:
        model = License
        fields = '__all__'