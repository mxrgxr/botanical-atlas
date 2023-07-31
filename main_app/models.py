from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ('light', 'Light'),
    ('water', 'Water'),
    ('air', 'Air'),
    ('nutrients', 'Nutrients'),
    ('temperature', 'Temperature'),
)

class GrowthCondition(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True)
    descriptor = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.get_category_display()} - {self.descriptor}"

    def get_absolute_url(self):
        return reverse('growth_conditions_detail', kwargs={'pk': self.id})

# Create your models here.
class Plant(models.Model):
    common_name = models.CharField(max_length=50)
    genus = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    plant_type = models.CharField(max_length=50)
    endangered = models.BooleanField()
    growth_conditions = models.ManyToManyField(GrowthCondition)
    def __str__(self):
        return f'{self.common_name} ({self.id})'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

class CountryOfOrigin(models.Model):
    country_name = models.CharField(max_length=50)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.country_name} for plant {self.plant.common_name}"

    class Meta:
        ordering = ['country_name']

