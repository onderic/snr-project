# forms.py
from django import forms
from .models import PoolSpace

class PoolForm(forms.ModelForm):
    class Meta:
        model = PoolSpace
        fields = ['title', 'email', 'number', 'height', 'latitude', 'longitude', 'address', 'user']
