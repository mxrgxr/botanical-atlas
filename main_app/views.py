plants = [
    {
        "name": "Maxillaria sophronitis",
        "genus_species": "Maxillaria sophronitis (Rchb.f.) Garay",
        "conservation_status": "Least Concern",
        "plant_type": "Pseudobulbous epiphyte",
        "country_of_origin": "Colombia to Venezuela",
    },
    {
        "name": "Philodendron lazorii",
        "genus_species": "Philodendron lazorii Croat",
        "conservation_status": "Least Concern",
        "plant_type": "Climber",
        "country_of_origin": "Panama to NW. Colombia",
    },
    {
        "name": "Espeletia funckii",
        "genus_species": "Espeletia funckii Sch.Bip. ex Wedd.",
        "conservation_status": "Endangered",
        "plant_type": "Subshrub or shrub",
        "country_of_origin": "Colombia (Norte de Santander, Santander)",
    },
]

from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})