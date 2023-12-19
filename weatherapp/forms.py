from django import forms
from .models import contact

class contactform(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'