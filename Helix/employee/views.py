from django.shortcuts import render
from .models import Schedule
# Create your views here.

def schedule_view(request):

    obj = Schedule.objects.all().order_by('holiday' ,'start_Date', 'start_Time')

    return render()