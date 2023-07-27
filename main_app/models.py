from django.db import models
from django.urls import reverse

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=50)
    genus = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    plant_type = models.CharField(max_length=50)
    country_of_origin = models.CharField(max_length=20)
    endangered = models.BooleanField()
    def __str__(self):
        return f'{self.common_name} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})