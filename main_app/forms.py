from django.forms import ModelForm
from .models import CountryOfOrigin

class CountryOfOriginForm(ModelForm):
    class Meta:
        model = CountryOfOrigin
        fields = ['country_name']