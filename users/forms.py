from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.contrib import messages
from users.models import UserProfile


def validate_email(value):
    """Check if the email address already exists in the system"""
    if User.objects.filter(email=value).exists():
        raise ValidationError(f"{value} is taken.", params={'value': value})


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput(attrs={'class': 'form-control'})


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'First-Name',
                                                               }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Last-Name'
                                                              }))
    email = forms.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    # profile_pic = forms.ImageField TODO: Deal with images later
    job_title = forms.CharField(label='Job Title', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'job_title',
    }))

    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'job_title', 'public_profile']
