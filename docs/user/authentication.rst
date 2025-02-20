.. _authentication:

Authentication
==============

Basic Authentication
-------------------------

Standard BasicAuth, every request contains your username and password base64 encoded in the request header. The most
insecure, but simplest, way to authenticate. Remember to scope the user's ACLs to the minimum if using with automations.

    >>> client = pysnc.ServiceNowClient('dev00000', ('admin','password'))

OAuth Authentication
--------------------

OAuth2 password flow is currently supported and recommended - one must setup an OAuth Client to use.

    >>> from pysnc import ServiceNowClient
    >>> from pysnc.auth import ServiceNowOauth2
    >>> client_id = 'ac0dd3408c1031006907010c2cc6ef6d' # oauth_entity.client_id
    >>> secret = '...' # oauth_entity.client_secret
    >>> client = ServiceNowClient(server_url, ServiceNowOAuth2(username, password, client_id, secret))

This will use a users credentials to retrieve and store an OAuth2 auth and refresh token, sending your auth token with
every request and dropping your user and password from memory. If this sleeps for a long enough time your refresh token
may requiring re-auth.

JWT Authentication
------------------

Create a new [JWT Provider](https://docs.servicenow.com/en-US/bundle/tokyo-platform-security/page/administer/security/task/create-jwt-endpoint.html)
and use it with whomever generates your JWT tokens. Once you have your JWT you may use it to request a Bearer token for
standard auth:

    >>> auth = ServiceNowJWTAuth(client_id, client_secret, token)
    >>> client = ServiceNowClient(self.c.server, auth)

Wherein client_id and client_secret are the `oauth_jwt` record entry values and `token` is the JWT generated by your provider.

The token contains who are are logging in as - as such the PySNC library does not attempt to act as a provider. We do however
have an example of how that is done in the tests.

Requests Authentication
-----------------------

Ultimately any authentication method supported by python requests (https://2.python-requests.org/en/master/user/authentication/) can be passed directly to ServiceNowClient.

Should be flexible enough for any use-case.

Storing Passwords
-----------------

The keystore module is highly recommended. For example::

    import keyring

    def check_keyring(instance, user):
        passw = keyring.get_password(instance, user)
        return passw

    def set_keyring(instance, user, passw):
        keyring.set_password(instance, user, passw)

    if options.password:
        passw = options.password
        set_keyring(options.instance, options.user, passw)
    else:
        passw = check_keyring(options.instance, options.user)
        if passw is None:
            print('No Password specified and none found in keyring')
            sys.exit(1)

    client = pysnc.ServiceNowClient(options.instance, ServiceNowOAuth2(options.user, passw))
