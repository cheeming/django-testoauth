Django Login System
-------------------
The Django OAuth Toolkit makes use of the Django login system and we need
to deal with some URL endpoints.

They are specified in ```TestOAuth/urls.py``` and prefixed with
```accounts/```. I think they are pretty self explanatory and the sample
implementation is simple, you might need to write more code to make it
more useful.

Authorization Grant Types
-------------------------
Quick overview:
- Implicit: For web apps and mobile apps. Client Secret confidentiality can't be maintained.
- Authorization Code: For server side web apps. Client Secret confidentiality can be maintained. Able to use Refresh Token.

Testing OAuth2 - Implicit
-------------------------
1. Start Django server

        ./manage.py runserver

2. Add new application for OAuth. Go to http://127.0.0.1:8000/oauth2/applications/
  - Client type: public
  - Authorization Grant Type: implicit
  - Redirect URI: http://127.0.0.1:8000/oauth2-consumer/redirect-implicit/
3. Request OAuth authorization for the new app. Go to the following URL in
   your web browser, you will need to login, and you will need to URL encode
   the CLIENT_ID: http://127.0.0.1:8000/oauth2/authorize/?response_type=token&client_id=CLIENT_ID
  - Encode your CLIENT_ID with this: http://meyerweb.com/eric/tools/dencoder/
4. If all goes well, you will be redirected back to the registered
   Redirect URI with the access token, which is part of the URL fragment.
5. Since its passed back as a URL fragment, you will need to deal with
   using Javascript.
   There is a sample implementation: ```OAuth2ConsumerRedirectImplicitView```
   in ```TestOAuth/views.py``` file.

Testing OAuth2 - Authorization Code
-----------------------------------
1. Follow the similar steps are above, but change the following:
  - Redirect URI: http://127.0.0.1:8000/oauth2-consumer/redirect-authorization-code/APP_ID/
    - Replace APP_ID with the id (primary key) of the application object
  - Use this URL to request OAuth authorization: http://127.0.0.1:8000/oauth2/authorize/?response_type=code&client_id=CLIENT_ID
2. The sample implementation is: ```OAuth2ConsumerRedirectAuthorizationCodeView```
   in ```TestOAuth/views.py``` file.
3. The difference in the flow is we will get the Authorization Code first
   and use that to get the Access Token. We can use Refresh Token to get
   new Access Token. For Implicit grant type, we can't use Refresh Token.

Read up on OAuth2
-----------------
 * Good guide here: https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
 * Specific to Django OAuth Toolkit, https://django-oauth-toolkit.readthedocs.org/en/0.7.0/tutorial/tutorial_01.html
