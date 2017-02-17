from django.shortcuts import render
from django.http import HttpResponse
from api.scraping import scrapingreq
import django_filters
from rest_framework import viewsets, filters
from .models import animedb
from .serializer import animedbSerializer
# Create your views here.



def scraping(request,year,page,season):
    scrapingreq(str(year),str(page),str(season))
    return HttpResponse('done')



class animedbViewSet(viewsets.ModelViewSet):
    queryset = animedb.objects.all()
    serializer_class = animedbSerializer
    #filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('season','year',)