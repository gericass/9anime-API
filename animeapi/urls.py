"""animeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from api import views
from api.urls import router as anime_router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<year>\d+)/Winter/(?P<page>\d+)/$', views.scraping,{'season': 'Winter'}),
    url(r'^(?P<year>\d+)/Spring/(?P<page>\d+)/$', views.scraping,{'season': 'Spring'}),
    url(r'^(?P<year>\d+)/Summer/(?P<page>\d+)/$', views.scraping,{'season': 'Summer'}),
    url(r'^(?P<year>\d+)/Fall/(?P<page>\d+)/$', views.scraping,{'season': 'Fall'}),
    url(r'^(?P<year>\d+)/Unknow/(?P<page>\d+)/$', views.scraping,{'season': 'Unknow'}),

    url(r'^week/(?P<data>\d+)/(?P<year>\d+)/Winter/(?P<page>\d+)/$', views.week,{'season': 'Winter'}),
    url(r'^week/(?P<data>\d+)/(?P<year>\d+)/Spring/(?P<page>\d+)/$', views.week,{'season': 'Spring'}),
    url(r'^week/(?P<data>\d+)/(?P<year>\d+)/Summer/(?P<page>\d+)/$', views.week,{'season': 'Summer'}),
    url(r'^week/(?P<data>\d+)/(?P<year>\d+)/Fall/(?P<page>\d+)/$', views.week,{'season': 'Fall'}),
    url(r'^week/(?P<data>\d+)/(?P<year>\d+)/Unknow/(?P<page>\d+)/$', views.week,{'season': 'Unknow'}),

    url(r'^api/', include(anime_router.urls)),
]
