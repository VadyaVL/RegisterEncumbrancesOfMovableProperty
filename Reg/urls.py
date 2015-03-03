from django.conf.urls import patterns, include, url
from django.contrib import admin
import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
import restApi

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^personsrest/$', restApi.PersonList.as_view()),
    url(r'^personsrest/(?P<pk>\d+)/$', restApi.PersonDetail.as_view()),

    url(r'^addressrest/$', restApi.AddressList.as_view()),
    url(r'^addressrest/(?P<pk>\d+)/$', restApi.AddressDetail.as_view()),
    url(r'^typerest/$', restApi.TypeOfEncumbranceList.as_view()),
    url(r'^typerest/(?P<pk>\d+)/$', restApi.TypeOfEncumbranceDetail.as_view()),
    url(r'^viewrest/$', restApi.ViewEncumbranceList.as_view()),
    url(r'^viewrest/(?P<pk>\d+)/$', restApi.ViewEncumbranceDetail.as_view()),
    url(r'^typeregrest/$', restApi.TypeRegList.as_view()),
    url(r'^typeregrest/(?P<pk>\d+)/$', restApi.TypeRegDetail.as_view()),
    url(r'^currencyrest/$', restApi.TypeOfCurrencyList.as_view()),
    url(r'^currencyrest/(?P<pk>\d+)/$', restApi.TypeOfCurrencyDetail.as_view()),

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

    url(r'^person/', views.vPerson),
    url(r'^delete/person/(?P<id>\d+)/$', views.dPerson),
    url(r'^edit/person/(?P<id>\d+)/$', views.ePerson),
    url(r'^add/person/', views.aPerson),

    url(r'^add/', views.add),
    url(r'^encumbrance/', views.view),
    url(r'^delete/encumbrance/(?P<id>\d+)/$', views.delete),
    url(r'^edit/encumbrance/(?P<id>\d+)/$', views.edit),

    url(r'^home/', views.home),
    url(r'^', views.home),
)

#urlpatterns += [
#    url(r'^api-auth/', include('rest_framework.urls',
#                               namespace='rest_framework')),
#]

urlpatterns = format_suffix_patterns(urlpatterns)

