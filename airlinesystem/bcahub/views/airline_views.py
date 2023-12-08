from django.shortcuts import render, redirect , get_object_or_404


from bcahub.models import Traveller

from django.contrib import messages

def base(request): 
    data = Traveller.objects.raw('select * from bcahub_traveller')
    return render(request, 'pages/home.html', {'data': data})

def createtravel(request):
    return render(request,'pages/homecreate.html')

def store(request):
    air= Traveller()
    air.flight = request.POST.get('flight')
    air.timeFrame = request.POST.get('timeFrame')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.nrc = request.POST.get('nrc')
    air.gender = request.POST.get('gender')
    air.depature_port = request.POST.get('depature_port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_port = request.POST.get('arrival_port')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.save()
    messages.success(request,"New Travelling data Added Successfully")
    return redirect('/portal/pages/base')

def updateViewtravel(request,pk):
    air = Traveller.objects.get(id = pk)
    return render(request,'pages/homeedit.html',{'air':air})

def updatetravel(request,pk):
    air = Traveller.objects.get(id = pk)  
    air.flight = request.POST.get('flight')
    air.timeFrame = request.POST.get('timeFrame')
    air.name = request.POST.get('name')
    air.dob = request.POST.get('dob')
    air.nrc = request.POST.get('nrc')
    air.gender = request.POST.get('gender')
    air.depature_port = request.POST.get('depature_port')
    air.depature_date_time = request.POST.get('depature_date_time')
    air.arrival_port = request.POST.get('arrival_port')
    air.arrival_date_time = request.POST.get('arrival_date_time')
    air.save()
    messages.success(request,"Airline Customer Update Successfully")
    return redirect('/portal/pages/base')