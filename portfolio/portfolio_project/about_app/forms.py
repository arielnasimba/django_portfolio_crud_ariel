from django import forms 

from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description_1', 'job_title', 'description_2','birthday', 'website', 'phoneNumber', 'city', 'age', 'degree', 'email', 'isFreelance', 'description_3', 'imageProfile', 'job_title2']
        widgets = {
            'imageProfile': forms.FileInput()
        }