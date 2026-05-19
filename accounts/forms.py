from django import forms
from .models import Profile
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']

        widgets = {
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите телефон',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес',
                'rows': 3,
                'style': 'resize: none;',
            }),
        }

        labels = {
            'phone': 'Телефон',
            'address': 'Адрес',
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email',
            }),
        }

        labels = {
            'email': 'Email',
        }
