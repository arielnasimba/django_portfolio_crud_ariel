from django import forms 

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['street', 'streetNumber', 'city','cityNumber', 'email', 'phoneNumber']
