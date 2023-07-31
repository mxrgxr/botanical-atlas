from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>/', views.plants_detail, name='detail'),
    path('plants/create/', views.PlantCreate.as_view(), name='plants_create'),
    path('plants/<int:pk>/delete', views.PlantDelete.as_view(), name='plants_delete'),
    path('plants/<int:pk>/update', views.PlantUpdate.as_view(), name='plants_update'),
    path('plants/<int:plant_id>/add_country_of_origin/', views.add_country_of_origin, name='add_country_of_origin'),
    path('plants/<int:plant_id>/assoc_growth_condition/<int:growth_condition_id>/', views.assoc_growth_condition, name='assoc_growth_condition'),
    path('plants/<int:plant_id>/unassoc_growth_condition/<int:growth_condition_id>/', views.unassoc_growth_condition, name='unassoc_growth_condition'),
    path('growth_conditions/', views.GrowthConditionList.as_view(), name='growth_conditions_list'),
    path('growth_conditions/<int:pk>/', views.GrowthConditionDetail.as_view(), name='growth_conditions_detail'),
    path('growth_conditions/create/', views.GrowthConditionCreate.as_view(), name='growth_conditions_create'),
    path('growth_conditions/<int:pk>/delete/', views.GrowthConditionDelete.as_view(), name='growth_conditions_delete'),
    path('growth_conditions/<int:pk>/update/', views.GrowthConditionUpdate.as_view(), name='growth_conditions_update'),
]