from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views
from website.views import *

admin.autodiscover()

urlpatterns = patterns('website.views',
    url(r'^$', index, name='home'),
    url(r'^chisiamo/$', chisiamo, name='chisiamo'),
    url(r'^ilte/$', ilte, name='ilte'),
    url(r'^ilte/classificazione/$', classificazionete, name='classificazionete'),
    url(r'^ilte/ipaesidelte/$', ipaesidelte, name='ipaesidelte'),
    url(r'^inostrite/$', inostrite, name='inostrite'),
    url(r'^inostrite/(?P<titolo>\d+)/$', categoriate, name='categoriate'),
    url(r'^inostrite/(?P<titolo>\d+)/(?P<unte_id>\d+)$', unnostrote, name='unnostrote'),
    url(r'^ritodelte/$', ritodelte, name='ritodelte'),
    # url(r'^blog/$', BlogView.as_view()), 
    url(r'^dovesiamo/$', dovesiamo, name='dovesiamo'),
    url(r'^contatti/$', contatti, name='contact')
    )