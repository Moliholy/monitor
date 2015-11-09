from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # option for the browser
    # url(r'^cb/', include('cvmfs_browser.urls')),
    url(r'^', include('stratum0.urls')),
)
