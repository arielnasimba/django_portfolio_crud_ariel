from django.db import models

from django.core.validators import RegexValidator

# Create your models here.

class Contact(models.Model):
    street                  = models.CharField(max_length=60)
    streetNumber            = models.CharField( max_length=50)
    city                    = models.CharField(max_length=50)
    cityNumber              = models.CharField(max_length=50)
    email                   = models.EmailField( max_length=254)
    phoneNumber             = models.CharField(max_length=14, validators=[RegexValidator(r'^\d{1,10}$')])
    