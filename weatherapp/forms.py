from django import forms
from .models import contact
from captcha.fields import CaptchaField

class contactform(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model=contact
        fields='__all__'