from django import forms 

from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model   = Testimonial
        fields  = ['name','jobTitle', 'jobTitle2', 'self_description','image']
        widgets = {'image' : forms.FileInput() }

        