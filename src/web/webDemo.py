#coding:utf-8
'''
Created on Apr 24, 2017

@author: weiruibo
'''
import urllib2
import re


page=1
url='http://www.qiushibaike.com/8hr/page/'+str(page)

agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

user_agent={'User-Agent':agent}



requset=urllib2.Request(url,headers=user_agent)

response=urllib2.urlopen(requset)

content= response.read().decode('utf-8')
# 
# print content
pattern=re.compile('<div class="author clearfix">.*?<h2>(?P<title>.*?)</h2>.*?<div class="content">.*?<span>(?P<content>.*?)</span>.*?</div>.*?<div class="stats">.*?<i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash".*?<i class="number">(.*?)</i>(.*?)</a>.*?<div class="main-text">(.*?)<div class="likenum">',re.S)
# pattern=re.compile('<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats".*?i class="number">(.*?)</i>(.*?)</span>.*?<span class="dash".*?i class="number">(.*?)</i>(.*?)</a>',re.S) 

result=re.findall(pattern, content)
# result=re.search(pattern, content)
for item in result:
     
    print 'title:',item[0],'\n','content:',item[1],'\n',item[3],':',item[2],'\n',item[5],":",item[4],'\n','神评论:',item[6]
    print '--------------------------'
#     
# 
# if result:
#     print result.group(1)
#     print result.group(2)
#     print result.group(3)
#     print result.group(4)
#     print result.group(5)
#     print result.group(6)
#     print result.group(7)
#      
#      
#       
#      
# else:
#     print "Error"

