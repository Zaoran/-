from django.shortcuts import render
from dormitory.models import duty
# Create your views here.
def input(request):

    OurDuty = duty.objects.get(id=1)

    DutyDic = {}
    DutyDic['water'] = OurDuty.water
    DutyDic['rubbish'] = OurDuty.rubbish

    return render(request, "dormitory_input.html",DutyDic)

def WaterOutput(request):

    OurDuty = duty.objects.get(id=1)

    if OurDuty.water <= 3:
        OurDuty.water += 1
    else:
        OurDuty.water = 1

    OurDuty.save()

    return render(request, "dormitory_output.html")

def RubbishOutput(request):

    OurDuty = duty.objects.get(id=1)

    if OurDuty.rubbish <= 3:
        OurDuty.rubbish += 1
    else:
        OurDuty.rubbish = 1

    OurDuty.save()

    return render(request, "dormitory_output.html")

def information(request):
    return render(request, "dormitory_information.html")

