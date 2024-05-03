from django import forms 

from .models import Skills


class SkillsForm(forms.ModelForm):
    class Meta:
        model   = Skills
        fields  = ['name','level_skill']
