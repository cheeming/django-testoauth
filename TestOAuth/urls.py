from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from TestOAuth import views


urlpatterns = patterns('',
    # django admin
    url(r'^admin/', include(admin.site.urls)),

    # standard django login/logout
    (r'^accounts/profile/$', 'TestOAuth.views.profile'),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),

    # oauth2 provider
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    # API protected by the oauth2
    (r'^api/hello-world/$', views.ApiHelloWorld.as_view()),

    # oauth2 consumer (normally this would be in another server,
    # implemented by the API consumer)
    (r'^oauth2-consumer/redirect-implicit/$',
     views.OAuth2ConsumerRedirectImplicitView.as_view()),

    url(r'^oauth2-consumer/redirect-authorization-code/(?P<app_id>\d+)/$',
        views.OAuth2ConsumerRedirectAuthorizationCodeView.as_view(),
        name='oauth2_consumer_redirect_authorization_code'),
)
