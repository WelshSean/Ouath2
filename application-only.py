import os
import urllib
import base64

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


if __name__ == "__main__":

    a =  getCreds()
    print encodeConsumerInfo(a[0], a[1])