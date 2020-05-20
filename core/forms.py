from django import forms
from .models import *


class contact_form(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    emailid = forms.EmailField(widget=forms.EmailInput(), required=True, max_length=100)
    message = forms.CharField(widget=forms.TextInput(), required=True)

    class Meta():
        model = contact
        fields = ['name', 'emailid', 'message']
