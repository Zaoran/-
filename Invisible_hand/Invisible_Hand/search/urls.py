from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input),
    path('output/', views.output),
    path('FreshNameNumber/', views.FreshNameNumber),
]
