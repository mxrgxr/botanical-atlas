from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CountryOfOriginForm
from .models import Plant, GrowthCondition

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    country_of_origin_form = CountryOfOriginForm()
    growth_conditions = GrowthCondition.objects.all()
    associated_growth_conditions = plant.growth_conditions.all()
    available_growth_conditions = growth_conditions.exclude(id__in=associated_growth_conditions.values_list('id', flat=True))
    return render(request, 'plants/detail.html', {'plant': plant, 'country_of_origin_form': country_of_origin_form, 'associated_growth_conditions': associated_growth_conditions, 'available_growth_conditions': available_growth_conditions})

class PlantCreate(CreateView):
  model = Plant
  fields = ['common_name', 'genus', 'species', 'plant_type', 'endangered']

class PlantUpdate(UpdateView):
  model = Plant
  fields = ['common_name', 'genus', 'species', 'plant_type', 'endangered']

class PlantDelete(DeleteView):
  model = Plant
  success_url = '/plants'

def add_country_of_origin(request, plant_id):
  form = CountryOfOriginForm(request.POST)
  if form.is_valid():
    new_country = form.save(commit=False)
    new_country.plant_id = plant_id
    new_country.save()
  return redirect('detail', plant_id=plant_id)

def assoc_growth_condition(request, plant_id, growth_condition_id):
    plant = Plant.objects.get(id=plant_id)
    growth_condition = GrowthCondition.objects.get(id=growth_condition_id)
    plant.growth_conditions.add(growth_condition)
    return redirect('detail', plant_id=plant_id)

def unassoc_growth_condition(request, plant_id, growth_condition_id):
    plant = Plant.objects.get(id=plant_id)
    growth_condition = GrowthCondition.objects.get(id=growth_condition_id)
    plant.growthconditions.remove(growth_condition)
    return redirect('detail', plant_id=plant_id)

class GrowthConditionList(ListView):
    model = GrowthCondition
    template_name = 'main_app/growth_conditions_list.html'

class GrowthConditionDetail(DetailView):
    model = GrowthCondition
    template_name = 'main_app/growth_conditions_detail.html'

class GrowthConditionCreate(CreateView):
    model = GrowthCondition
    fields = '__all__'
    template_name = 'main_app/growth_conditions_form.html'

class GrowthConditionUpdate(UpdateView):
    model = GrowthCondition
    fields = '__all__'
    template_name = 'main_app/growth_conditions_form.html'

class GrowthConditionDelete(DeleteView):
    model = GrowthCondition
    success_url = '/growth_conditions'
    template_name = 'main_app/growth_conditions_confirm_delete.html'