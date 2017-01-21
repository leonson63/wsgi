from django.conf.urls import patterns, include, url
from qa.views import test

urlpatterns = patterns('qa.views',
    url(r'^login/', 'test', name='login'),
    url(r'^signup/', 'test', name='signup'),
    url(r'^question/([^/]+)/', 'test', name='id'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^view/', test, name='view'),   
    url(r'^/', test, name='all'),
)
