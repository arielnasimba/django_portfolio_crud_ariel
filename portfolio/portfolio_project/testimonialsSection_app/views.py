from django.shortcuts import render, redirect
from .models import Testimonial
from .forms import TestimonialForm

# Create your views here.
def read_testimonials(request):
    listTestimonials = Testimonial.objects.all()
    return render(request, 'backend/testimonials_Section/readTestimonials.html', {'listTestimonials': listTestimonials})



def add_testimonial(request):
    listTestimonials = Testimonial.objects.all()
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/all-Testimonials/")
    else:
        form = TestimonialForm()
    return render(request,'backend/testimonials_Section/addTestimonial.html',{'form': form, 'listServices_':listTestimonials})


def delete_testimonial(request,id):
	member = Testimonial.objects.get(id=id)
	member.delete()
	return redirect('allTestimonials') 



def update_testimonial(request, id):
	product = Testimonial.objects.get(id=id)
	form = TestimonialForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()
		return redirect('allTestimonials')
	return render(request, 'backend/testimonials_Section/addTestimonial.html' ,  {'form' : form})


def testimonial_details(request, id):
	testimonial_infos = Testimonial.objects.get(id=id)
	return render(request, 'backend/testimonials_Section/testimonial_detail.html', {'testimonialInfo' : testimonial_infos})

