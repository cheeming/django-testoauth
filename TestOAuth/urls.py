from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from TestOAuth.views import OAuth2ConsumerRedirectImplicitView
from TestOAuth.views import OAuth2ConsumerRedirectAuthorizationCodeView


urlpatterns = patterns('',
    # django admin
    url(r'^admin/', include(admin.site.urls)),

    # oauth2 provider
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # standard django login/logout
    (r'^accounts/profile/$', 'TestOAuth.views.profile'),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),

    # oauth2 consumer
    (r'^oauth2-consumer/redirect-implicit/$',
     OAuth2ConsumerRedirectImplicitView.as_view()),

    url(r'^oauth2-consumer/redirect-authorization-code/(?P<app_id>\d+)/$',
        OAuth2ConsumerRedirectAuthorizationCodeView.as_view(),
        name='oauth2_consumer_redirect_authorization_code'),
)
