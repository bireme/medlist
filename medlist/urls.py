from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.defaults import patterns, include, url

from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medlist.views.home', name='home'),
    # url(r'^medlist/', include('medlist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/iahx/?$', 'medlist.api.views.iahx'),
    url(r'^medicine/(\d+)/?$', 'medlist.directory.views.show_medicine'),
)

# static files in development

if settings.LOCAL:
    urlpatterns += staticfiles_urlpatterns()
