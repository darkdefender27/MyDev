from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', include('appOne.urls')),
	url(r'^appOne/', include('appOne.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
#    url(r'^hi/$', 'appOne.views.say_hi', name='hi'),
#    url(r'^hello/$', 'appOne.views.hello', name='hello'),
#    url(r'^index/$', 'appOne.views.index', name='index'),
)
