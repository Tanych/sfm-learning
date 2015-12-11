# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/54/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/23/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # /polls/12/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]