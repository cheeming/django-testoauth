Django Login System
-------------------
The Django OAuth Toolkit makes use of the Django login system and we need
to deal with some URL endpoints.

They are specified in ```TestOAuth/urls.py``` and prefixed with
```accounts/```. I think they are pretty self explanatory and the sample
implementation is simple, you might need to write more code to make it
more useful.

Testing OAuth2
--------------
1. Start Django server
    manage.py runserver
2. Add new application for OAuth. Go to http://127.0.0.1:8000/oauth2/applications/
  - Client type: public
  - Authorization Grant Type: implicit
  - Redirect URI: http://127.0.0.1:8000/oauth2-consumer/redirect-implicit/
3. Request OAuth authorization for the new app. Go to the following URL in
   your web browser, you will need to login, and you will need to URL encode
   the CLIENT_ID:
    http://127.0.0.1:8000/oauth2/authorize/?response_type=token&client_id=CLIENT_ID
  - Encode your CLIENT_ID with this: http://meyerweb.com/eric/tools/dencoder/
4. If all goes well, you will be redirected back to the registered
   Redirect URI with the access token, which is part of the URL fragment.
5. Since its passed back as a URL fragment, you will need to deal with
   using Javascript.
   There is a sample implementation ```OAuth2ConsumerRedirectImplicitView``` in ```TestOAuth/views.py``` file.

Read up on OAuth2
-----------------
 * Good guide here: https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
 * Specific to Django OAuth Toolkit, https://django-oauth-toolkit.readthedocs.org/en/0.7.0/tutorial/tutorial_01.html
