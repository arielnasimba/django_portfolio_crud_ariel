from django.shortcuts import render
import skillsSection_app.models as skillsModel
import servicesSection_app.models as servicesModel

# Create your views here.

def indexPage_(request):
    
    list_services = servicesModel.Service.objects.all()
    list_skills = skillsModel.Skills.objects.all()          # =======> List of alls skills
    
    return render(request, 'frontend/index.html', { 'list_skills' : list_skills, 
                                                   'list_services' : list_services} )

