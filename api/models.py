from django.db import models

# Create your models here.

class animedb(models.Model):
    SEASON_SET = (
        ('Winter','冬'),
        ('Spring','春'),
        ('Summer','夏'),
        ('Fall','秋'),
        ('Unknow','未定義'),
    )
    YEAR_SET = (
        ('2017','2017'),
        ('2016','2016'),
        ('2015','2015'),
        ('2014','2014'),
        ('2013','2013'),
    )
    WEEKDAY_SET = (
        ('0','月'),
        ('1','火'),
        ('2','水'),
        ('3','木'),
        ('4','金'),
        ('5','土'),
        ('6','日'),
    )
    title =  models.CharField('アニメタイトル',max_length=500)
    title_jp = models.CharField('アニメタイトル（日本語）',max_length=500)
    year = models.CharField('放送年',max_length=500,choices=YEAR_SET)
    season = models.CharField('シーズン',max_length=500,choices=SEASON_SET)
    weekday = models.CharField('曜日',max_length=500,choices=WEEKDAY_SET,default=0)
    url = models.CharField('URL',max_length=500)
    page = models.CharField('ページ',max_length=500,default=1)

    def __str__(self):
        return self.title_jp



