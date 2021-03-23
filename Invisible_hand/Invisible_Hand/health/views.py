from django.shortcuts import render
from . import draw
from health.models import HealthCheck

# Create your views here.
def input(request):
    return render(request, "health_input.html")

def output(request):
    
    date = request.GET['date']
    leukocyte = request.GET['leukocyte']
    platelet = request.GET['platelet']
    neutrophil = request.GET['neutrophil']
    CA199 = request.GET['CA199']
    CA125 = request.GET['CA125']
    CEA = request.GET['CEA']

    if date == '':
        draw.draw()
        return render(request, "health_output.html")

    if leukocyte == '':
    	leukocyte = '-1'

    if platelet == '':
    	platelet = '-1'

    if neutrophil == '':
    	neutrophil = '-1'

    if CA199 == '':
    	CA199 = '-1'

    if CA125 == '':
    	CA125 = '-1'

    if CEA == '':
    	CEA = '-1'

    HealthData = HealthCheck(date = date,leukocyte = leukocyte,
                            platelet = platelet,neutrophil = neutrophil,
                            CA199 = CA199,CA125 = CA125,CEA=CEA)
    HealthData.save()

    draw.draw()

    return render(request, "health_output.html")