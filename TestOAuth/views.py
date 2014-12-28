from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView
from urllib.parse import parse_qs
from pprint import pformat


@login_required
def profile(request):
    return HttpResponse('You are logged in')


class OAuth2ConsumerRedirectImplicitView(TemplateView):
    template_name = 'oauth2_consumer/redirect_implicit.html'

    def post(self, request):
        postback_value = request.POST.get('postback_value')
        postback_dict = parse_qs(postback_value)
        return HttpResponse('<pre>postback_dict (values URL decoded):\n\n{}</pre>'.format(pformat(postback_dict)))
