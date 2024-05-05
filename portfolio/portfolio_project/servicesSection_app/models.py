from django.db import models

# Create your models here.


class Service(models.Model):
    icon_choices = [
        ('bi-briefcase', 'Briefcase'),
        ('bi-card-checklist', 'Card Checklist'),
        ('bi-bar-chart', 'Bar Chart'),
        ('bi-binoculars', 'Binoculars'),
        ('bi-brightness-high', 'Brightness High'),
        ('bi-calendar4-week', 'Calendar Week'),
    ]
    
    # icon = choices()
    title = models.CharField(max_length=40)
    description = models.TextField()
    icon = models.CharField(max_length=100, choices=icon_choices, default='bi-briefcase')