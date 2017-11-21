"""week1_1105 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from app1.views import get_es_url, update_es_address
from focus import views
from focus import urls as focus_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app1/get_es_url/$', get_es_url),
    url(r'^app1/update_es_address/$', update_es_address),
    url(r'^focus/', include(focus_urls)),
    url(r'^$', views.index, name='index'),
]
