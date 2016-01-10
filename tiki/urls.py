from django.conf.urls import patterns, url

from tiki import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

