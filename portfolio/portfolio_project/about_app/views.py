from django.shortcuts import render, redirect
from django.urls import reverse

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
    
    
def profile_details(request, id):
	profile_infos = Profile.objects.get(id=id)
	return render(request, 'backend/profile_Section/profile_detail.html', {'profile_infos' : profile_infos})


def update_profile(request, id):
	product = Profile.objects.get(id=id)
	form = ProfileForm(request.POST, request.FILES or None, instance=product)
	if form.is_valid():
		form.save()


        # return redirect(reverse('profile_details', kwargs={'id': id}))
  
		return redirect(reverse('profile_details', kwargs={'id': id}))

	return render(request, 'backend/profile_Section/updateProfile.html' ,  {'form' : form})




		# return redirect('profile_details')
