from .forms import Registration, Contactus
from django import forms

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'