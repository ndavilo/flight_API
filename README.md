# flight_API
Flight Services API with Django Rest Framework

Adding Token
Goto settings and add 'rest_framework.authtoken'
REST_FRAMEWORK={
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ]
}
Got urls and add path('api-token-auth/', obtain_auth_token, name="api_token_auth")
and from rest_framework.authtoken.views import obtain_auth_token