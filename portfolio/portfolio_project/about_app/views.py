from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def add_profile(request):
    images = Profile.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect("addImage")
    else:
        form = ProfileForm()
        return render(request,'backend/addProfile.html',{'form':form, 'images':images})