from django.conf.urls import patterns, include, url
from qa.views import all, popular, question, test, ask, tologin, signup

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^aaa/', include(admin.site.urls)),
    url(r'^login/', tologin, name='login'),
    url(r'^signup/', signup, name='signup'),
    url(r'^question/(?P<id>\d+)/', question, name='question-id'),
    url(r'^ask/', ask, name='ask'),
    url(r'^popular/', popular, name='question-popular'),
    url(r'^new/', test, name='new'),   
    url(r'^', all, name='question-all'),
)
