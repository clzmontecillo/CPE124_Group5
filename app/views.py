from django.shortcuts import render, redirect
from django.http import HttpResponse
import os
from django.db import connection
from .models import Sensor
from .models import Thresh
from multiprocessing import Process
from app.tyh import DataInsert as D
import sqlite3

class MainView:
    
    def ins(self):
        while True:
            instance = D()
            instance.insert()

    def __init__(self):
        pass
    
    def update(self, request):
        if request.method != 'POST':
            return redirect('/')
        
        
        tmp = request.POST['temp']
        hmd = request.POST['humid']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE app_thresh SET thresh_temp = %s", [str(tmp)])
            cursor.execute("UPDATE app_thresh SET thresh_humidity = %s", [str(hmd)])
            
        print("EXECUTED")
        return redirect('/')
    
    def index(self,request):
 
        cursor = connection.cursor()
        cursor.execute("select * from app_sensor")
        row = cursor.fetchone()

        print(row[1],row[2])
        context = { 'temperature': row[1],
        'humidity': row[2]
        }
        
        return render(request, 'dashboard.html', context)
    

print("k3k")
M = MainView()
Process(target=M.ins).start()


