"""medlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, re_path, include
from medlist import settings

from api import views as api_views
from main import views as main_views
from list import views as list_views
from directory import views as directory_views
from evidence import views as evidence_views
from history import views as history_views
from utils import views as utils_views

admin.site.site_header = 'MEDLIST'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='home'),
    path('close_window', main_views.close_window, name='close_window'),

    re_path(r'^api/get_sections/?$', api_views.get_sections, name='get_sections'),

    re_path(r'^list/(?P<id>\d+)/?$', list_views.show_list, name='show_list'),
    re_path(r'^list/compare/?$', list_views.compare, name='compare'),

    re_path(r'^medicine/(?P<id>\d+)/?$', directory_views.show_medicine, name='show_medicine'),

    re_path(r'^evidence/(?P<id>\d+)/?$', evidence_views.show, name='show_evidence'),

    re_path(r'^history/(?P<id>\d+)/?$', history_views.save_history, name='save_history'),
    re_path(r'^show_history/(?P<id>\d+)/?$', history_views.show_history, name='show_history'),

    re_path(r'^get_scientific_production/?$', utils_views.get_scientific_production, name='get_scientific_production'),

    # internationalization
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    #re_path(r'^cookie-lang/?$', 'utils.views.cookie_lang'),
]
