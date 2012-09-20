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
    url(r'^api/get_hierarchy_relation/(\d+)/?$', 'medlist.api.views.get_hierarchy_relation'),
    url(r'^api/get_section_parents/(\d+)/?$', 'medlist.api.views.get_section_parents'),
    url(r'^api/get_pharmaceutical_forms/?$', 'medlist.api.views.get_pharmaceutical_forms'),
    url(r'^api/get_sections/?$', 'medlist.api.views.get_sections'),
    url(r'^api/index/?$', 'medlist.api.views.index'),
    
    url(r'^medicine/(?P<id>\d+)/?$', 'medlist.directory.views.show_medicine'),
    
    url(r'^list/(?P<id>\d+)/?$', 'medlist.list.views.show_list'),
    url(r'^list/compare/?$', 'medlist.list.views.compare'),

    url(r'^evidence/(?P<id>\d+)/?$', 'medlist.evidence.views.show'),

    # internationalization
    url(r'^i18n/', include('django.conf.urls.i18n')),

    url(r'^$', 'medlist.main.views.index'),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += patterns('',
        url(r'^rosetta/', include('rosetta.urls')),
    )

# static files in development
if settings.LOCAL:
    urlpatterns += staticfiles_urlpatterns()
