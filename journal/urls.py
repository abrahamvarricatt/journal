from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^tiki/', include('tiki.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('tiki.urls')),  # defaults
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

