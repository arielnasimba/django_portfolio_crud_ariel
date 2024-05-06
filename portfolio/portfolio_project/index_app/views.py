from django.shortcuts import render
import skillsSection_app.models as skillsModel
import servicesSection_app.models as servicesModel
import testimonialsSection_app.models as testimonialsModel

# Create your views here.

def indexPage_(request):
    list_testimonials = testimonialsModel.Testimonial.objects.all()     # =======> List of all testimonials
    list_services = servicesModel.Service.objects.all()                 # =======> List of all services
    list_skills = skillsModel.Skills.objects.all()                      # =======> List of all skills
    
    return render(request, 'frontend/index.html', { 'list_skills'           : list_skills, 
                                                    'list_services'         : list_services,
                                                    'list_testimonials'     : list_testimonials
                                                    }
                  )

