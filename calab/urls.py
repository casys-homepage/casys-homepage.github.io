"""calab URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from core import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^home$', core_views.index),
    url(r'^home/$', core_views.index),
    url(r'^home/index.html', core_views.index),
    url(r'^home/members.html', core_views.members),
    url(r'^home/album.html', core_views.album),
    url(r'^home/research.html', core_views.research),
    url(r'^home/publications.html', core_views.publications),
    url(r'^home/projects.html', core_views.projects),
    url(r'^home/contact.html', core_views.contact),
    url(r'^index.html', core_views.index),
    url(r'^members.html', core_views.members),
    url(r'^album.html', core_views.album),
    url(r'^research.html', core_views.research),
    url(r'^publications.html', core_views.publications),
    url(r'^projects.html', core_views.projects),
    url(r'^contact.html', core_views.contact),
    url(r'^~([a-zA-Z0-9_]*)/papers/(?P<paper_name>[a-zA-Z0-9_\-]*.pdf)', core_views.papers),
    url(r'^~([a-zA-Z0-9_]*)$', core_views.redirect_to_personal_page),
    url(r'^~([a-zA-Z0-9_]*)/$', core_views.personal),
    url(r'^~([a-zA-Z0-9_]*)/([a-zA-Z0-9_]*.html)$', core_views.personal),
    url(r'^~([a-zA-Z0-9_]*)/([a-zA-Z0-9_\-./]*)$', core_views.personal),
    url(r'^supe2rs3cret7dm1n', admin.site.urls),
    url(r'^software.html', include('software.urls')),
    url(r'^home/software.html', include('software.urls')),
    url(r'^google69fb8370d742f02f.html', core_views.google_validation),
]
