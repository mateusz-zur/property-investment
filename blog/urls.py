from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/', views.register),
    url(r'^investments/', views.investments),
    url(r'^save-investment/(?P<investment_id>\d+)/$', views.write_investment_to_file, name='save-investment'),
    url(r'^read-investment/(?P<investment_id>\d+)/$', views.read_investment_from_file, name='read-investment'),
]
