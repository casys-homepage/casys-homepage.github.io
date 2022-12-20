# coding=utf-8
from django.conf.urls import url

from software.views import SoftwareListView

urlpatterns = [
    url(r'^$', SoftwareListView.as_view(), name='software'),
]

