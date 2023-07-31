from django.contrib import admin
from .models import Plant, GrowthCondition, CountryOfOrigin

# Register your models here.
admin.site.register(Plant)
admin.site.register(GrowthCondition)
admin.site.register(CountryOfOrigin)
