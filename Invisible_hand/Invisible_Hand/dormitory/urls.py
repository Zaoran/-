from django.urls import path
from . import views

urlpatterns = [
    path('input/',views.input),
    path('water_output/',views.WaterOutput),
    path('rubbish_output/',views.RubbishOutput),
    path('information/',views.information),
]
