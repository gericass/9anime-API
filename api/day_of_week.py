from .models import animedb
from bs4 import BeautifulSoup
import urllib.request
import time
import re
from datetime import datetime

def getweekday(year,page,season):
    s = animedb.filter(year=str(year),season=str(season),page=str(page))
    link = []

    for i in s:
        link.append(i.url)

    for lk in link:
        url = lk
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        hizuke = ''

        hi = []

        for dt in soup.find_all("div",id="servers"):
            for a in dt.find_all("a"):
                hi.append(a['data-title'])

        dates = hi[0].split(" ")

        hizuke += dates[2]

        if dates[0] == 'Jan':
            hizuke += ',01,'
        elif dates[0] == 'Feb':
            hizuke += ',02,'
        elif dates[0] == 'Mar':
            hizuke += ',03,'
        elif dates[0] == 'Apr':
            hizuke += ',04,'
        elif dates[0] == 'May':
            hizuke += ',05,'
        elif dates[0] == 'Jun':
            hizuke += ',06,'
        elif dates[0] == 'Jul':
            hizuke += ',07,'
        elif dates[0] == 'Aug':
            hizuke += ',08,'
        elif dates[0] == 'Sep':
            hizuke += ',09,'
        elif dates[0] == 'Oct':
            hizuke += ',10,'
        elif dates[0] == 'Nov':
            hizuke += ',11,'
        elif dates[0] == 'Dec':
            hizuke += ',12,'

        hizuke += dates[1].replace(",","")

        yobi = datetime.strptime(hizuke,"%Y,%m,%d").weekday()

        if yobi == 6:
            p = animedb.objects.filter(url=lk)
            p.weekday = str(yobi)
            p.save()
        else:
            yobi+=1
            p = animedb.objects.filter(url=lk)
            p.weekday = str(yobi)
            p.save()


        time.sleep(0.8)