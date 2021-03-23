import numpy as np
import matplotlib.pyplot as plt
from health.models import HealthCheck
import time
from pathlib import Path
import os

plt.switch_backend('agg')

def draw():

    BASE_DIR = Path(__file__).resolve().parent.parent
    start_time = '2020-07-17'
    lower = [[3.5,3.5],[100,100],[1.8,1.8],[0,0],[0,0],[0,0]]
    upper = [[9.5,9.5],[350,350],[6.3,6.3],[35,35],[35,35],[5,5]]
    data = HealthCheck.objects.all().order_by('date')

    for dat in data:
        dat.date = str(dat.date)
    
    #try:
    #白细胞绘图
    HealthData = []
    for dat in data:
        if dat.leukocyte!='-1':
            HealthData.append(dat)

    date = []
    blood = []

    for health in HealthData:
        end_time = health.date
        start = time.mktime(time.strptime(start_time,'%Y-%m-%d'))
        end = time.mktime(time.strptime(end_time,'%Y-%m-%d'))
        date.append(int((end - start)/(24*60*60)))
        blood.append(float(health.leukocyte))

    StartEnd = [date[0],date[len(date)-1]]

    plt.plot(date,blood)
    plt.plot(date,blood,'o')
    plt.plot(StartEnd,lower[0])
    plt.plot(StartEnd,upper[0])
    plt.savefig(os.path.join(BASE_DIR, 'statics','images','leukocyte.jpg'))
    plt.close('all')

    #血小板绘图
    HealthData = []
    for dat in data:
        if dat.platelet!='-1':
            HealthData.append(dat)

    date = []
    blood = []

    for health in HealthData:
        end_time = health.date
        start = time.mktime(time.strptime(start_time,'%Y-%m-%d'))
        end = time.mktime(time.strptime(end_time,'%Y-%m-%d'))
        date.append(int((end - start)/(24*60*60)))
        blood.append(float(health.platelet))

    StartEnd = [date[0],date[len(date)-1]]

    plt.plot(date,blood)
    plt.plot(date,blood,'o')
    plt.plot(StartEnd,lower[1])
    plt.plot(StartEnd,upper[1])
    plt.savefig(os.path.join(BASE_DIR, 'statics','images','platelet.jpg'))
    plt.close('all')

    #中性细胞绘图
    HealthData = []
    for dat in data:
        if dat.neutrophil!='-1':
            HealthData.append(dat)

    date = []
    blood = []

    for health in HealthData:
        end_time = health.date
        start = time.mktime(time.strptime(start_time,'%Y-%m-%d'))
        end = time.mktime(time.strptime(end_time,'%Y-%m-%d'))
        date.append(int((end - start)/(24*60*60)))
        blood.append(float(health.neutrophil))

    StartEnd = [date[0],date[len(date)-1]]

    plt.plot(date,blood)
    plt.plot(date,blood,'o')
    plt.plot(StartEnd,lower[2])
    plt.plot(StartEnd,upper[2])
    plt.savefig(os.path.join(BASE_DIR, 'statics','images','neutrophil.jpg'))
    plt.close('all')

    #CA199绘图
    HealthData = []
    for dat in data:
        if dat.CA199!='-1':
            HealthData.append(dat)

    date = []
    blood = []

    for health in HealthData:
        end_time = health.date
        start = time.mktime(time.strptime(start_time,'%Y-%m-%d'))
        end = time.mktime(time.strptime(end_time,'%Y-%m-%d'))
        date.append(int((end - start)/(24*60*60)))
        blood.append(float(health.CA199))

    StartEnd = [date[0],date[len(date)-1]]

    plt.plot(date,blood)
    plt.plot(date,blood,'o')
    plt.plot(StartEnd,lower[3])
    plt.plot(StartEnd,upper[3])
    plt.savefig(os.path.join(BASE_DIR, 'statics','images','CA199.jpg'))
    plt.close('all')

    #CA125绘图
    HealthData = []
    for dat in data:
        if dat.CA125!='-1':
            HealthData.append(dat)

    date = []
    blood = []

    for health in HealthData:
        end_time = health.date
        start = time.mktime(time.strptime(start_time,'%Y-%m-%d'))
        end = time.mktime(time.strptime(end_time,'%Y-%m-%d'))
        date.append(int((end - start)/(24*60*60)))
        blood.append(float(health.CA125))

    StartEnd = [date[0],date[len(date)-1]]

    plt.plot(date,blood)
    plt.plot(date,blood,'o')
    plt.plot(StartEnd,lower[4])
    plt.plot(StartEnd,upper[4])
    plt.savefig(os.path.join(BASE_DIR, 'statics','images','CA125.jpg'))
    plt.close('all')

    #CEA绘图
    HealthData = []
    for dat in data:
        if dat.CEA!='-1':
            HealthData.append(dat)

    date = []
    blood = []

    for health in HealthData:
        end_time = health.date
        start = time.mktime(time.strptime(start_time,'%Y-%m-%d'))
        end = time.mktime(time.strptime(end_time,'%Y-%m-%d'))
        date.append(int((end - start)/(24*60*60)))
        blood.append(float(health.CEA))

    StartEnd = [date[0],date[len(date)-1]]

    plt.plot(date,blood)
    plt.plot(date,blood,'o')
    plt.plot(StartEnd,lower[5])
    plt.plot(StartEnd,upper[5])
    plt.savefig(os.path.join(BASE_DIR, 'statics','images','CEA.jpg'))
    plt.close('all')

    #except:
        #pass
