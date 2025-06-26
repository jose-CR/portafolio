from django import forms
from .models import UserProfile, ContactMe
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'description', 'github', 'linkedin'
        ]

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = UserProfile
        fields = [
            'username', 'first_name', 'last_name', 'email', 'description', 'github', 'linkedin'
        ]

class ContactMeForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = [
            'user_name', 'user_email', 'user_message'
        ]