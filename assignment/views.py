from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

import requests
import pandas as pd
from datetimerange import DateTimeRange
import json

# Create your views here.

def Shift(df,start,end,production_name):

    a=df[df["time"].between(start,end)][production_name]
    count=0
    for i in a:
        if str(i)=='True':
            count+=1
    return count

def home(request):
    df=pd.read_json('C:/Users/subho/Desktop/sample_json_1.json')
    

    production1_A_count=Shift(df,'2021-01-28 06:00:00','2021-01-28 14:00:00','production_A')
    production2_A_count=Shift(df,'2021-01-28 14:00:00','2021-01-28 20:00:00','production_A')
    production3_A_count=Shift(df,'2021-01-28 20:00:00','2021-01-28 06:00:00','production_A')

    production1_B_count=Shift(df,'2021-01-28 06:00:00','2021-01-28 14:00:00','production_B')
    production2_B_count=Shift(df,'2021-01-28 14:00:00','2021-01-28 20:00:00','production_B')
    production3_B_count=Shift(df,'2021-01-28 20:00:00','2021-01-28 06:00:00','production_B')

    dict_shift={
    "shiftA" :{ "production_A_count" :production1_A_count, "production_B_count" :production1_B_count},
    "shiftB" :{ "production_A_count" :production2_A_count, "production_B_count" :production2_B_count},
    "shiftC" :{ "production_A_count" :production3_A_count, "production_B_count" :production3_B_count},}
    json_string=json.dumps(dict_shift)

    return render(request, 'first.html',{'response': json_string,'name':"Question 1"})

