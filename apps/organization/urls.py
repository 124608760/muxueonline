# _*_ encoding:utf-8 _*_
__author__ = 'xyx'
__date__ = '2017-7-13 23:04'

from django.conf.urls import url, include

from .views import OrgView

urlpatterns=[
    url(r'list/$',OrgView.as_view(), name='org_list'),
]