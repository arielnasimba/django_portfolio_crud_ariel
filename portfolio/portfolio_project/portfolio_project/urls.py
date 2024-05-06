"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from about_app import views as aboutViews
from index_app import views as indexViews
from skillsSection_app import views as SkillsViews
from servicesSection_app import views as ServicesViews
from testimonialsSection_app import views as testimonialsViews
from contactSection_app import views as ContactViews
from portfolioSection_app import views as PortfolioViews
from hero_app import views as heroViews

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexViews.indexPage_ , name="home"),
    
    
    path('addProfile/', aboutViews.add_profile, name="addProfile"),
    
    
    #  <=====================================  Hero Section  =====================================>    #
    
    path('hero-details/<int:id>', heroViews.hero_details, name="hero_details"),                     #  ===> read all Profile
    path('hero-edit/update/<int:id>', heroViews.update_hero, name="updateHero"),                  #  ===> update Profile
    #  <=====================================  Profile Section  =====================================>    #
    
    path('profile-details/<int:id>', aboutViews.profile_details, name="profile_details"),                     #  ===> read all Profile
    path('profile-edit/update/<int:id>', aboutViews.update_profile, name="updateProfile"),   #  ===> update Profile
    
    
    #  <=====================================  Testimonials Section  =====================================>    #
    
    path('addTestimonial/', testimonialsViews.add_testimonial, name="addTestimonial"),                          #  ===> add testimonial
    path('all-Testimonials/', testimonialsViews.read_testimonials, name="allTestimonials"),                     #  ===> read all testimonial
    path('all-Testimonials/update/<int:id>', testimonialsViews.update_testimonial, name="updateTestimonial"),   #  ===> update testimonial
    path('testimonial-detail/<int:id>', testimonialsViews.testimonial_details, name='testimonial_details' ),    #  ===> details testimonial
    path('Testimonials/<int:id>/destroy', testimonialsViews.delete_testimonial , name="deleteTestimonial"),     #  ===> delete testimonial
    
    #  <=====================================  Portfolio Section  =====================================>    #
    
    path('addProject/', PortfolioViews.add_project, name="addProject"),                          #  ===> add testimonial
    path('all-projects/', PortfolioViews.read_projects, name="allProjects"),                     #  ===> read all testimonial
    path('all-projects/update/<int:id>', PortfolioViews.update_project, name="updateProject"),   #  ===> update testimonial
    path('project-detail/<int:id>', PortfolioViews.project_details, name='project_details' ),    #  ===> details testimonial
    path('project/<int:id>/destroy', PortfolioViews.delete_project , name="deleteProject"),     #  ===> delete testimonial
     
    #  <=====================================  Skills Section  =====================================>    #
    
    path('addSkills/', SkillsViews.add_skill, name="addSkills"),                                                #  ===> add skills
    path('all-Skills/', SkillsViews.read_skills, name="allSkills"),                                             #  ===> read all skills
    path('all-Skills/update/<int:id>', SkillsViews.update_skill, name="updateSkills"),                          #  ===> update skills
    path('skill-detail/<int:id>', SkillsViews.skill_details, name='skill_details' ),                            #  ===> details skill
    path('all-Skills/<int:id>/destroy', SkillsViews.delete_skill , name="deleteSkills"),                        #  ===> delete skill
    
    #  <===================================== Services Section =====================================>           #
    
    path('all-Services/', ServicesViews.read_services, name="allServices"),                                     #  ===> read all service
    path('addService/', ServicesViews.add_service, name="addService"),                                          #  ===> add service
    path('all-Services/update/<int:id>', ServicesViews.update_service, name="updateService"),                   #  ===> update service
    path('service-detail/<int:id>', ServicesViews.service_details, name='service_details' ),                    #  ===> details service
    path('all-Services/<int:id>/destroy', ServicesViews.delete_service , name="deleteService"),                 #  ===> delete service
    
    
    #  <===================================== Contact Section =====================================>           #
    
    # path('all-Services/', ServicesViews.read_services, name="allServices"),                                     #  ===> read all service
    # path('addService/', ServicesViews.add_service, name="addService"),                                          #  ===> add service
    path('contacts/update/<int:id>', ContactViews.update_contact, name="updateContact"),                   #  ===> update service
    path('contact-detail/<int:id>', ContactViews.contact_details, name='contact_details' ),                       #  ===> details service
    # path('all-Services/<int:id>/destroy', ServicesViews.delete_service , name="deleteService"),                 #  ===> delete service
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
