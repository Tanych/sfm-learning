"""learningsite URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.conf import settings
from weiboapp import views
import os

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'weiboapp.views.index', name='index'),
    url(r'^add/$', 'weiboapp.views.add', name='add'),
    url(r'^add/(\d+)/(\d+)/$', 'weiboapp.views.add2', name='add2'),

    """
    # url(r'^weibo/(?P<path>.*)$','learningsite.views.index')
    url(r'^weibo/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.STATIC_ROOT, 'weibo'), 'show_indexes': True}),

    # for weibo app testing

    url(r'^add_done/$', views.add_done),
"""
]
