from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import RegexValidator
# Create your models here.


class Profile(models.Model):
    
    DEGREE_CHOICES = [
    ("MA", "Master"),
    ("BAC", "Bachelor"),
    ("SD", "Secondary diploma"),
    ("ND", "No diploma")
    ]
    description_1   = models.CharField(default=10, max_length=150)
    job_title       = models.CharField(max_length=60)
    description_2   = models.CharField(default=10, max_length=100)
    birthday        = models.DateField( auto_now=False)
    website         = models.URLField( max_length=60)
    phoneNumber     = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    city            = models.CharField( max_length=40)
    age             = models.IntegerField(
        validators=[
            MinValueValidator(16),
            MaxValueValidator(67),
        ]
    )
    degree          = models.CharField( choices=DEGREE_CHOICES, max_length=50)
    email           = models.EmailField( max_length=54)
    isFreelance     = models.BooleanField()
    description_3   = models.TextField(default=10, max_length=200 )
    imageProfile    = models.ImageField( null=False ,upload_to="profiles_images/")
    # skill           = models.ForeignKey(".Model", verbose_name=_(""), on_delete=models.CASCADE, blank=True, null=True)    