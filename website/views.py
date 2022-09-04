from rest_framework import viewsets
import json
from django.http import JsonResponse
from django.http import HttpResponse
import numpy as np 
import joblib  

from django.views.decorators.csrf import csrf_exempt


from.serializers import PersonSerializer, SpeciesSerializer
from .models import Person, Species

@csrf_exempt
def location(request):
   if request.method == "POST":
      data = request.POST.dict()
      print(data)
      location = data['Location']
      district = data['District']
      print(location)
      print(district)
         
      # print (request.body.decode('utf-8'))
      # data1 = data['Success']
      # print(data1)
      return JsonResponse({'success':location,'code':district})
   else:
      return JsonResponse({'success':1})


@csrf_exempt
def cropprediction(request):
   
   if request.method == "POST":
      data = request.POST.dict()
      N = data['N']
      P = data['P']
      K = data['K']
      humidity = data['humidity']
      temp = data['temp']
      rainfall = data['rainfall']
      ph = data['ph']

      user_inputs = np.array[N,P,K,humidity,temp,rainfall,ph].reshape(1,-1)
      model = joblib.load('../notebooks/RFR_Model.sav')
      result = model.predict(user_inputs)
      print(data)
      

      return JsonResponse({'success':str(result[0]),'code':0})
   else:
      return JsonResponse({'success':1})