from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('jonathanschen.views',
	url(r'^$', 'index'),
	url(r'^about/$', 'about'),
	url(r'^portfolio/$', 'portfolio'),
	url(r'^blog/$', 'blog'),
	url(r'^contact/$', 'contact'),
	url(r'^thanks/$', 'thanks'),
	url(r'^month/(\d+)/(\d+)/$', 'month'),
    url(r'^admin/', include(admin.site.urls)),
)
