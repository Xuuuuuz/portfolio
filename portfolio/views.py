#coding=utf-8
_date_ = '2019/3/12 17:36'
from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys=Gallery.objects
    return render(request,'home.html',{'gallerys':gallerys})