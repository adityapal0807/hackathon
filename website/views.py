from rest_framework import viewsets
import json
from django.http import JsonResponse
from django.http import HttpResponse

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
      print(data)
      

      return JsonResponse({'success':1,'code':0})
   else:
      return JsonResponse({'success':1})