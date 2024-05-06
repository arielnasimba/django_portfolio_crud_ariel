
# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Project
from .forms import ProjectForm

# Create your views here.


def read_projects(request):
    listProjects = Project.objects.all()
    return render(request, 'backend/portfolio_Section/readProjects.html', {'listProjects': listProjects})

def add_project(request):
    images = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect("allProjects")
    else:
        form = ProjectForm()
        return render(request,'backend/portfolio_Section/addProject.html',{'form':form, 'images':images})
    
    
def project_details(request, id):
	profile_infos = Project.objects.get(id=id)
	return render(request, 'backend/profile_Section/profile_detail.html', {'profile_infos' : profile_infos})


def update_project(request, id):
	product = Project.objects.get(id=id)
	form = ProjectForm(request.POST, request.FILES or None, instance=product)
	if form.is_valid():
		form.save()


        # return redirect(reverse('profile_details', kwargs={'id': id}))
  
		return redirect(reverse('profile_details', kwargs={'id': id}))

	return render(request, 'backend/profile_Section/updateProfile.html' ,  {'form' : form})


def delete_project(request,id):
	member = Project.objects.get(id=id)
	member.delete()
	return redirect('allProjects') 

