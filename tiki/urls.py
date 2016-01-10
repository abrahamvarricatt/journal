from django.conf.urls import patterns, url

from tiki import views

urlpatterns = patterns('',
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
    url(r'^$', views.index, name='index'),
)

