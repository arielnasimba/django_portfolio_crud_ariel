from django.shortcuts import render, redirect
from .models import Skills
from .forms import SkillsForm
# Create your views here.


def add_skill(request):
    listSkills = Skills.objects.all()

    if request.method == 'POST':
        form = SkillsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SkillsForm()
    return render(request,'backend/addSkills.html',{'form': form, 'listSkills':listSkills})


def read_skills(request):
    listSkills = Skills.objects.all()

    return render(request,'backend/readSkills.html',{'listSkills':listSkills})



def delete_skill(request,id):
	member = Skills.objects.get(id=id)
	member.delete()
	return redirect('/') 


def update_skill(request, id):
	product = Skills.objects.get(id=id)
	form = SkillsForm(request.POST or None, instance=product)
	if form.is_valid():
		form.save()
		return redirect('allSkills')
	return render(request, 'backend/updateSkills.html' ,  {'form' : form})


def skill_details(request, id):
	skill_infos = Skills.objects.get(id=id)
	return render(request, 'backend/skill_detail.html', {'skillInfo' : skill_infos})

