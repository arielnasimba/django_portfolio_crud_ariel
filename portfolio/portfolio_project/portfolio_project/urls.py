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

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexViews.indexPage_ , name="home"),
    
    
    path('addProfile/', aboutViews.add_profile, name="addProfile"),
    
    
    path('addSkills/', SkillsViews.add_skill, name="addSkills"),   # add skills
    
    path('all-Skills/', SkillsViews.read_skills, name="allSkills"),     # read all skills
    
    path('all-Skills/update/<int:id>', SkillsViews.update_skill, name="updateSkills"),  # update skills
    path('skill-detail/<int:id>', SkillsViews.skill_details, name='skill_details' ),    #details skill

    
    path('all-Skills/<int:id>/destroy', SkillsViews.delete_skill , name="deleteSkills"),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
