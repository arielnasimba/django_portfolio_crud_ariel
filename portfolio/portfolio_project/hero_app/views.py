from django.shortcuts import render, redirect
from .models import Hero
from .forms import HeroForm
from django.urls import reverse


# Create your views here.


def hero_details(request, id):
	hero_infos = Hero.objects.get(id=id)
	return render(request, 'backend/hero_Section/hero_detail.html', {'hero_infos' : hero_infos})


def update_hero(request, id):
	product = Hero.objects.get(id=id)
	form = HeroForm(request.POST, request.FILES or None, instance=product)
	if form.is_valid():
		form.save()


        # return redirect(reverse('profile_details', kwargs={'id': id}))
  
		return redirect( reverse('hero_details', kwargs={'id': id}) )

	return render(request, 'backend/hero_Section/updateHero.html' ,  {'form' : form})


