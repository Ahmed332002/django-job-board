from django import forms
from .models import Apply
from django.forms import ModelForm


class ApplyForm(ModelForm):
    class Meta:
        model = Apply
        fields = ('name', 'email', 'website', 'cv', 'cover_letter')
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            }),
            'website': forms.URLInput(attrs={
                'placeholder': 'Website/Portfolio link',
                'class': 'form-control'
            }),
            'cv': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'inputGroupFile03',
                'aria-describedby': 'inputGroupFileAddon03'
            }),
        }