from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.urls import reverse


# Create your views here.
def contact_details(request, id):
	contact_infos = Contact.objects.get(id=id)
	return render(request, 'backend/contact_Section/contact_detail.html', {'contact_infos' : contact_infos})


def update_contact(request, id):
	product = Contact.objects.get(id=id)
	form = ContactForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()

  
		return redirect(reverse('contact_details', kwargs={'id': id}))

	return render(request, 'backend/contact_Section/updateContact.html' ,  {'form' : form})
