import urllib2
from urllib import urlencode
import cookielib

request=urllib2.Request('http://www.baidu.com');
# response = urllib2.urlopen(request)

try:
    value={'username':'test','password':'test'}
    data=urlencode(value)
    resquest=urllib2.Request('http://www.baidu.com',data)
    response=urllib2.urlopen(resquest)
    print response.read()
    
except urllib2.URLError, e:
    print e.reason

url="http://www.baidu.com"

cookie=cookielib.CookieJar();
handlers=urllib2.HTTPCookieProcessor(cookie)
opener=urllib2.build_opener(handlers)
response=opener.open(url, data, 100)

filename='cookie.txt'
cookie2=cookielib.MozillaCookieJar(filename)

handler=urllib2.HTTPCookieProcessor(cookie2)

opener=urllib2.build_opener(handler);
response=opener.open(url)

cookie2.save(filename, True, True)


