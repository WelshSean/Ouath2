import os
import urllib
import base64
import requests

# URL to HTTP POST to in order to get a bearer token
TWITTER_BEARER_URL = 'https://api.twitter.com/oauth2/token/'

def getCreds():
    """
    Pull in Twitter Consumer Key and Secret from the environment and return as a tuple
    :return: (ConsumerKey, ConsumerSecret)
    """
    key = os.environ['ConsumerKey']
    secret = os.environ['ConsumerSecret']

    return (key, secret)

def encodeConsumerInfo(key, secret):
    """
    Encode Consumer Key and Secret for access to Twitter API via Application only Oauth2 route.
    https://dev.twitter.com/oauth/application-only
    :param key: Twitter Consumer Key
    :param secret: Twitter Consumer Secret
    :return: Base64 encoded creds base64enc(urlenc(key):urlenc(secret))
    """
    string = urllib.quote_plus(key) + ":" + urllib.quote_plus(secret)
    return base64.b64encode(bytes(string))

def obtainBearerToken(consumerCreds):
    headers = { 'Authorization' : 'Basic ' + consumerCreds  ,
                'Content-Type' : 'application/x-www-form-urlencoded;charset=UTF-8'}
    payload = urllib.urlencode({'grant_type' : 'client_credentials'})
    print "Headers: " + str(headers)

    r = requests.post(TWITTER_BEARER_URL, headers = headers, params = payload)

    print "RESPONSE: " + str(r.status_code)

    responseJSON = r.json()

    if responseJSON["token_type"] == "bearer":
        print "w00t"
        return responseJSON["access_token"]
    else:
        print "boo"



if __name__ == "__main__":
    creds =  getCreds()
    encodedCreds = encodeConsumerInfo(creds[0], creds[1])
    bearerToken = obtainBearerToken(encodedCreds)
    print "Bearer token: " + str(bearerToken)