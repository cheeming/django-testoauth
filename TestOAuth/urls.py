from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TestOAuth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # implement the standard django login/logout
    (r'^accounts/profile/$', 'TestOAuth.views.profile'),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),

    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

)
