from django.conf.urls import patterns, include, url
from django.contrib import admin
from callmanage.views import home,test,test2,test3

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vecallmanager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home),
    url(r'^test/$', test),
    url(r'^test2/$', test2),
    url(r'^test3/$', test3),
)
