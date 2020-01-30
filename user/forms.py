from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        widgets = {
            "username": forms.TextInput(attrs={"readonly": True})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'favourite_posts', 'favourite_comments']