from django.shortcuts import render

from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from .models import reading, table_reading
from datetime import datetime

# Create your views here.
@api_view(["GET"])
def add_data(request):
    info=request.GET
    if info.get('data')==None:
        return JsonResponse({'status', 'Bad request'})
    data = reading()
    # data.time_of_recording = info['rid']
    data.reading_value = info['data']
    if info.get('time_of_reading') !=None:
        data.time_of_recording = datetime.strptime(info['time_of_reading'], '%Y-%m-%d %H:%M:%S')
    else:
        data.time_of_recording = datetime.now()
    if info.get('reading_details') !=None:
        data.reading_details = info['reading_details']
    data.save()
    return JsonResponse({'Status':'Record Sucessfully Saved'})

@api_view(["GET"])
def add_reading_data(request):
    info=request.GET
    if info.get('data')==None:
        return JsonResponse({'status', 'Bad request'})
    data = table_reading()
    # data.time_of_recording = info['rid']
    data.reading_value = info['data']
    if info.get('time_of_reading') !=None:
        data.time_of_recording = datetime.strptime(info['time_of_reading'], '%Y-%m-%d %H:%M:%S')
    else:
        data.time_of_recording = datetime.now()
    if info.get('reading_details') !=None:
        data.reading_details = info['reading_details']
    data.save()
    return JsonResponse({'Status':'Record Sucessfully Saved'})


from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")