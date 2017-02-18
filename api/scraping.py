from bs4 import BeautifulSoup
import urllib.request
import time
import re
from api.models import animedb
from datetime import datetime
#start = time.time()

def scrapingreq(year,page,season):
  #try:
    animedb.objects.filter(year=str(year),season=str(season),page=str(page)).delete()

    anititle = []
    link =[]
    title_jp = []
    #monthday = ["月","火","水","木","金","土","日"]
    dayofweek = []

    ajaurl = []

    url = 'https://9anime.to/filter?language=subbed&release[]=' + str(year)+ '&season[]='+ str(season) + '&page=' + str(page)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, "lxml")


    for tit in soup.find_all(class_="name"):
        anititle.append(tit.text)
        link.append(tit['href'])

    for aja in soup.find_all(class_="poster"):
        ajaurl.append('https://9anime.to/'+aja['data-tip'])
        # time.sleep(1)


    for i in range(len(ajaurl)):
        url = ajaurl[i]
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, "lxml")

        pre = []
        truetitle = ''

        for tit in soup.find_all("div",class_='meta'):
            for spa in tit.find_all("span"):
                pre.append(spa.text)

        pre2 = pre[4].replace("\n","")

        title = re.sub('\s{2}',"",pre2).split("; ")
        if len(title)>=2:
            if int(len(title[len(title)-1]))>=50:
                for tit in soup.find_all(class_="title"):
                    tt = tit.text
                truetitle = re.sub('(\s2.+$)','',tt)
                title_jp.append(truetitle)
            else:
                title_jp.append(title[len(title)-1])

        else:
            if int(len(title[0]))>=50:
                for tit in soup.find_all(class_="title"):
                    tt = tit.text
                truetitle = re.sub('(\s2.+$)','',tt)
                title_jp.append(truetitle)
            else:
                title_jp.append(title[0])
        time.sleep(0.1)

    #for wk in link:
        url2 = link[i]
        req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0'})
        response2 = urllib.request.urlopen(req2)
        html2 = response2.read()
        soup2 = BeautifulSoup(html2, "lxml")

        hizuke = ''

        hi = []

        for dt in soup2.find_all("div",id="servers"):
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
            dayofweek.append(yobi)
        else:
            yobi+=1
            dayofweek.append(yobi)
        time.sleep(1)


    for i in range(len(anititle)):
        tit = anititle[i]
        lin = link[i]
        titj = title_jp[i]
        sea = str(season)
        pg = str(page)
        yr = str(year)
        wd = str(0)
        db = animedb(title=tit,title_jp=titj,year=yr,season=sea,weekday=wd,url=lin,page=pg)
        db.save()

    return 'done'

  #except:
   #   return 'error'