from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from about_app import models as aboutModel


# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length=150)
    level_skill = models.IntegerField(default=1, null=False,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100),
        ]
    )
    # profileID = models.ForeignKey( aboutModel.Profile, on_delete=models.CASCADE)
    
    