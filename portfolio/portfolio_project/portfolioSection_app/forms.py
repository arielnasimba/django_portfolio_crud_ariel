from django import forms 

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_title', 'description','deadline', 'website_link', 'category', 'imageProject']
        widgets = {
            'imageProject': forms.FileInput()
        }