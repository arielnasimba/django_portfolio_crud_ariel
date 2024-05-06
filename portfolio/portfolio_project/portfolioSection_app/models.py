
# Create your models here.
from django.db import models

# Create your models here.


class Project(models.Model):
    
    CAT_CHOICES = [
    ("app", "Application"),
    ("card", "Cards"),
    ("web", "Development Web")
    ]
    project_title           = models.CharField(max_length=60)
    description             = models.TextField()
    deadline                = models.DateField(auto_now=False)
    website_link            = models.URLField( max_length=80)
    category          = models.CharField( choices=CAT_CHOICES, max_length=50)
    imageProject    = models.ImageField( null=False ,upload_to="images/projects_images/")
