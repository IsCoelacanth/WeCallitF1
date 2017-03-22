from django.http import HttpResponseRedirect, HttpResponse
from . models import *
from django.db import connection
from django.shortcuts import render
from django.http import Http404
from datetime import datetime
# Create your views here.

def index(request):
    now = datetime.utcnow()
    names = []
    for i in range(3):
        names.append( 'Meme/images/'+ str(now.day) + '-' + str(now.month) + '-' \
                    +str(now.year) + '-' + (str(i+1)) +'.png')
    context = {
        'image':names,
    }
    return render(request,'/home/codebox/FunProjects/Site_1/WeCallItF1/Meme/templates/Meme/index.html',context)
