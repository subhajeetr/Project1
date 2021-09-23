from django.shortcuts import render
from django.http import HttpResponse
import json
import pandas as pd
from datetimerange import DateTimeRange
import datetime


# Create your views here.

def Utilization_hours(df2,start,end,runtime_name):
    a=df2[df2["time"].between(start,end)][runtime_name]
    runtime_count=0
    downtime_count=0
    for i in a:
        if int(i)<=1021:
            runtime_count=runtime_count+int(i)
        else:
            a=int(i)-1021
            runtime_count=runtime_count+1021
            downtime_count=downtime_count+a
    return runtime_count,downtime_count

def home(request):
    df2=pd.read_json ('C:/Users/subho/Desktop/sample_json_2.json')
    
    runtime,downtime=Utilization_hours(df2,'2021-01-28 06:00:00','2021-01-28 14:00:00','runtime')
    print(runtime,downtime)

    run_sec=int(runtime)
    down_sec=int(downtime)

    runtime_hours = str(datetime.timedelta(seconds=run_sec))
    downtime_hours = str(datetime.timedelta(seconds=down_sec))

    print(runtime_hours,downtime_hours)

    utilisation=(runtime)/(runtime+downtime)*100
    utilisation_hours="{:.2f}".format(utilisation)

    runtime_dict={
            "runtime" : runtime_hours,
            "downtime": downtime_hours,
            "utilisation":utilisation_hours
        }
    json_runtime=json.dumps(runtime_dict)
    return render(request, 'first.html',{'response': json_runtime,'name':"Question 2"})
    