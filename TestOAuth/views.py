from urllib.parse import urlencode, parse_qs
from urllib.request import urlopen
from pprint import pformat
import json

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from oauth2_provider.models import Application
from oauth2_provider.views.generic import ProtectedResourceView


@login_required
def profile(request):
    return HttpResponse('You are logged in')


#######
# API #
#######
class ApiHelloWorld(ProtectedResourceView):
    def get(self, request):
        return HttpResponse('OK hello world')


###################
# OAuth2 Consumer #
###################
# Normally this would be in another server,
# implemented by the API consumer

class OAuth2ConsumerRedirectImplicitView(TemplateView):
    template_name = 'oauth2_consumer/redirect_implicit.html'

    def post(self, request):
        postback_value = request.POST.get('postback_value')
        postback_dict = parse_qs(postback_value)
        return HttpResponse('<pre>postback_dict (values URL decoded):\n\n{}</pre>'.format(pformat(postback_dict)))


class OAuth2ConsumerRedirectAuthorizationCodeView(View):
    def get(self, request, app_id):
        # get the authorization code
        code = request.GET.get('code')
        html = 'app_id: {}, code: {}'.format(app_id, code)

        app = Application.objects.get(id=app_id)

        # using the authorization code, request for access token
        params = urlencode({
            'client_id': app.client_id,
            'client_secret': app.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': 'http://127.0.0.1:8000{}'.format(reverse('oauth2_consumer_redirect_authorization_code', args=[app.id])),
        }).encode('utf8')

        access_token_str = urlopen('http://127.0.0.1:8000/oauth2/token/', params).read()
        access_token_info = json.loads(access_token_str.decode('utf8'))

        html += '<pre>access_token:\n\n{}</pre>'.format(pformat(access_token_info))

        return HttpResponse(html)
