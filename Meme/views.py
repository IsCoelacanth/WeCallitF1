from django.http import HttpResponseRedirect, HttpResponse
from . models import *
from . forms import *
from django.db import connection
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
# Create your views here.

def index(request):
    now = datetime.utcnow()
    names = []
    for i in range(3):
        names.append( 'Meme/images/'+ str(now.day) + '-' + '0' + str(now.month) + '-' \
                    +str(now.year) + '-' + (str(i+1)) +'.png')
        # names.append( 'Meme/images/'+ '22' + '-' + '03' + '-' \
                    # + '2017' + '-' + (str(i+1)) +'.png')
    context = {
        'image':names,
    }
    return render(request,'/home/codebox/FunProjects/Site_1/WeCallItF1/Meme/templates/Meme/index.html',context)

def prevday(request):
    form = dateForm(request.POST)
    context = {
        'form' : form,
    }

    if form.is_valid():
        data = form.cleaned_data
        data = [v for v in data.values()]
        data = data[0].split('-')
        print(data)
        return HttpResponseRedirect('Previous/'+data[0]+'/'+data[1]+'/'+data[2]+'/')
    # return HttpResponse("HELLO")
    return render(request, 'Meme/prevday.html',context)

def pday(request, dd , mm , yy ):
    if (validDate(dd,mm)):
        print(dd,mm,yy)
        names = []
        for i in range(3):
            names.append( 'Meme/images/'+ dd + '-' + mm + '-' \
                        + yy + '-' + (str(i+1)) +'.png')
        context = {
            'image':names,
        }
        return render(request,'/home/codebox/FunProjects/Site_1/WeCallItF1/Meme/templates/Meme/index.html',context)

def validDate(dd,mm):
    if(int(dd) >= 1 and int(dd) <= 31):
        if(int(mm) >=1 and int(mm) <= 12):
            return True
    return False
