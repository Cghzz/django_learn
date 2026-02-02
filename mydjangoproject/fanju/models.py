from django.db import models

# Create your models here.
class Django1(models.Model):
    name = models.CharField(max_length=200)
    time_class=models.CharField(max_length=200)

