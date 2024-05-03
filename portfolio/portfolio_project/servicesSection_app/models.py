from django.db import models

# Create your models here.


class Service(models.Model):
    
    
    # icon = choices()
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=150)