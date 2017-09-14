from django.shortcuts import render
from django.http import HttpResponse
from api.scraping import scrapingreq
import django_filters
from rest_framework import viewsets, filters
from .models import animedb
from .serializer import animedbSerializer
from .day_of_week import getweekday
# Create your views here.


def initdb(request):
    animedb.objects.filter(year="2017").delete()
    return HttpResponse("init db 2017")

def scraping(request,year,page,season):
    res = scrapingreq(str(year),str(page),str(season))
    return HttpResponse(res)

def week(request,data,year,page,season):
    res = getweekday(str(year),str(page),str(season),int(data))
    #res2 = getweekday(str(year),str(page),str(season),res)
    return HttpResponse(res)

class animedbViewSet(viewsets.ModelViewSet):
    queryset = animedb.objects.all()
    serializer_class = animedbSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('season','year',)