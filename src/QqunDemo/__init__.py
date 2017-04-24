#coding:utf-8
import urllib2
import urllib
import cookielib



url_qzone="https://h5.qzone.qq.com/mqzone/index"
# url_qzone="ui.ptlogin2.qq.com/cgi-bin/login?style=37&appid=728041403&s_url=http%3A%2F%2Finfoapp.3g.qq.com%2Fg%2Fusercenter%2Fcommon2.jsp%3Fsid%3D%26aid%3Duser_subshow&low_login=1&low_login_hour=4321&daid=261"

targer_url='http://client.qun.qq.com/cgi-bin/feeds/get_feed?_=1493020349781&fid=291eea0e0000000087cdf958c7da0200&qid=250224169&gsi=QiYYwxQ4Vaxi0h4WvFJtWu4cxdL-c3nZwHykn7rcMnqQ3AXwZJUj_jEhZQfHDp9tLsnzfPtb3EMhiqF8Ms8ROQ%40%40&bkn=71825306'

value={'u':'609044092','p':'xiezhuna1431214'}

data=urllib.urlencode(value)

filename="myCookie.txt"

cookie=cookielib.MozillaCookieJar(filename)

user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)"

handler={'user-agent':user_agent,
        'Accept':'application/javascript, */*;q=0.8'
}


request=urllib2.Request(url_qzone,data=data)

opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response=opener.open(request, data)

print response.read()

cookie.save(filename, True, True)

cookie.load(filename, True, True)

req=urllib2.Request(targer_url)
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

response=opener.open(req)

print response.read()


