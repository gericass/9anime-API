import time
import api.scraping as sc
import api.day_of_week as DoW

def process():

    season = ["Winter","Spring","Summer","Fall","Unknow"]
    page = [1,2,3,4,5]
    page2 = [1,2]
    year = [2017]#,2016,2015,2014,2013]
    while True:
        for i in year:
            for j in season:
                for k in page:
                    try:
                        sc.scrapingreq(i,k,j)
                    except:
                        print(str(i)+j+str(k)+" error")
        for i in page2:
            for j in year:
                for k in season:
                    for m in page:
                        try:
                            DoW.getweekday(j,m,k,i)
                        except:
                            print(str(i)+str(j)+k+str(m)+" error")
        time.sleep(86400) #一日(86400秒)おきに実行