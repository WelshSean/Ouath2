from httmock import urlmatch, HTTMock
import requests

@urlmatch(netloc=r'(.*\.)?google\.com$')
def google_mock(url, request):
    return 'Feeling lucky, punk?'

with HTTMock(google_mock):
    r = requests.get('http://google.com/')
print r.content  # 'Feeling lucky, punk?'