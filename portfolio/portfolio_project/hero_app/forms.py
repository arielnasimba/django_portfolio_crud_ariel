from django import forms 

from .models import Hero


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['name', 'last_name','word1','word2', 'word3', 'word4', 'image']
        widgets = {
            'image': forms.FileInput()
        }
        
        