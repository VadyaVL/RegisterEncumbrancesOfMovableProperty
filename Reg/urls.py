from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^currency/', views.vCurrency),
    url(r'^delete/currency/(?P<id>\d+)/$', views.dCurrency),
    url(r'^edit/currency/(?P<id>\d+)/$', views.eCurrency),
    url(r'^add/currency/', views.aCurrency),

    url(r'^view/', views.vView),
    url(r'^delete/view/(?P<id>\d+)/$', views.dView),
    url(r'^edit/view/(?P<id>\d+)/$', views.eView),
    url(r'^add/view/', views.aView),

    url(r'^type/', views.vType),
    url(r'^delete/type/(?P<id>\d+)/$', views.dType),
    url(r'^edit/type/(?P<id>\d+)/$', views.eType),
    url(r'^add/type/', views.aType),

    url(r'^typereg/', views.vTypeReg),
    url(r'^delete/typereg/(?P<id>\d+)/$', views.dTypeReg),
    url(r'^edit/typereg/(?P<id>\d+)/$', views.eTypeReg),
    url(r'^add/typereg/', views.aTypeReg),

    url(r'^address/', views.vAddress),
    url(r'^delete/address/(?P<id>\d+)/$', views.dAddress),
    url(r'^edit/address/(?P<id>\d+)/$', views.eAddress),
    url(r'^add/address/', views.aAddress),

    url(r'^add/', views.add),

    url(r'^home/', views.home),
    url(r'^', views.home),
)
