from django.shortcuts import render, redirect
from .models import Service
from .forms import ServicesForm

def read_services(request):
    listServices = Service.objects.all()
    return render(request, 'backend/services_Section/readServices.html', {'listServices': listServices})


def add_service(request):
    listServices_ = Service.objects.all()

    if request.method == 'POST':
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/all-Services/")
    else:
        form = ServicesForm()
    return render(request,'backend/services_section/addService.html',{'form': form, 'listServices_':listServices_})



def delete_service(request,id):
	member = Service.objects.get(id=id)
	member.delete()
	return redirect('allServices') 


def service_details(request, id):
	service_infos = Service.objects.get(id=id)
	return render(request, 'backend/services_Section/service_detail.html', {'serviceInfo' : service_infos})



def update_service(request, id):
	product = Service.objects.get(id=id)
	form = ServicesForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()
		return redirect('allServices')
	return render(request, 'backend/services_Section/updateService.html' ,  {'form' : form})
