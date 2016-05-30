import json
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import logging
# http://code.google.com/apis/urlshortener/v1/getting_started.html
# This works:
#   curl https://www.googleapis.com/urlshortener/v1/url \
#    -H 'Content-Type: application/json'\
#    -d '{"longUrl": "http://www.peterbe.com"}'
#
URL = 'https://www.googleapis.com/urlshortener/v1/url'

def shorten(url):
    #data = urllib.urlencode({'longUrl': url})
    data = json.dumps({'longUrl': url})
    headers = {'Content-Type': 'application/json'}
    req = urllib.request.Request(URL, data, headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    logging.info("Shorten %r --> %s" % (url, the_page))
    struct = json.loads(the_page)
    return struct['id']

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        if '://' in url:
            print(shorten(url))
