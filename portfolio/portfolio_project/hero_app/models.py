from django.db import models

# Create your models here.


class Hero(models.Model):
    name        = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    word1       = models.CharField(max_length=25)
    word2       = models.CharField(blank=True ,max_length=25)
    word3       = models.CharField(blank=True ,max_length=25)
    word4       = models.CharField(blank=True ,max_length=25)
    image       = models.ImageField( null=False ,upload_to="images/hero_images/")
