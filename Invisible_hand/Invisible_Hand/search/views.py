from django.shortcuts import render
from django.http import HttpResponse
from . import search,fresh
from search.models import NameNumber

#输入
def input(request):
    return render(request,"search_input.html")

#输出
def output(request):

    #读取用户输入
    number = request.GET['number']
    start = request.GET['start']
    end = request.GET['end']

    if number == '':
      number = '000001'
    if start == '':
      start = '2020-01-01'
    if end == '':
      end = '2020-12-31'

    #输出计算结果
    name,low,high,days,BigDays,first,stage_1,second,stage_2,third,stage_3,fourth,stage_4 = search.search(number,start,end)

    output = {"name":name,
              "number":number,
              "start":start,
              "end":end,
              "low":low,
              "high":high,
              "days":days,
              "BigDays":BigDays,
              "first":first,
              "stage_1":stage_1,
              "second":second,
              "stage_2":stage_2,
              "third":third,
              "stage_3":stage_3,
              "fourth":fourth,
              "stage_4":stage_4,}

    return render(request,"search_output.html",output)

#更新数据库
def FreshNameNumber(request):

    #删除现有数据
    NameNumber.objects.all().delete()

    NewNameNumber = fresh.NameNumber()
    for i in range(0,len(NewNameNumber['name'])):
        ticker = NameNumber(name = NewNameNumber['name'][i],
                            number = NewNameNumber['number'][i],
                            exchange = NewNameNumber['exchange'][i])
        ticker.save()
    return render(request,"fresh.html")