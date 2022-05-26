
from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns=[
    re_path(r'^$',views.welcome,name = 'welcome'),
    re_path(r'^$',views.news_of_day,name='newsToday'),
    re_path(r'^search/', views.search_results, name='search_results')
    re_path(r'^article/(\d+)',views.article,name ='article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

