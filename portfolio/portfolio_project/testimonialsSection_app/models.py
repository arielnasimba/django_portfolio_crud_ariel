from django.db import models

# Create your models here.

class Testimonial(models.Model):
    name                = models.TextField(null=False, max_length=50)
    jobTitle            = models.CharField( null=False,max_length=50)
    jobTitle2           = models.CharField( blank=True, max_length=50)
    self_description    = models.TextField()
    image               = models.ImageField(upload_to="images/testimonial_images/")
    