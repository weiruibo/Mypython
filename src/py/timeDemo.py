#coding:utf-8
'''
Created on Apr 23, 2017

@author: weiruibo

    time包
'''
import time
import datetime

print time.time();
print time.clock()


print 'start'
print 'weak up'

st=time.gmtime();
print st

st=time.localtime()
print st
s=time.mktime(st)
print s

print '现在是',st[0],'年',st[1],'月',st[2],'号',st[3],":",st[4],":",st[5],'星期',st[6],'2017年到现在已经',st[7],"天了"


''' datetime包 '''

t=datetime.datetime(st[0],st[1],st[2],st[3],st[4],st[5])
print t
print t.microsecond


t=datetime.datetime(2012,9,3,21,30)
t_next=datetime.datetime(2012,9,5,23,30)

delta1=datetime.timedelta(seconds=600)
delta2=datetime.timedelta(weeks=3)


''' 时间间隔对象(timedelta)''' 
print t+delta1
print t+delta2 # 一个时间点(datetime)加上一个时间间隔(timedelta)可以得到一个新的时间点(datetime)。

print t_next-t #两个时间点相减会得到一个时间间隔。

print t>t_next

str    = "output-1997-12-23-030000.txt" 
format = "output-%Y-%m-%d-%H%M%S.txt" 
t=datetime.datetime.strptime(str,format)
print t

print t_next.strftime(format)

'''

    时间，休眠
    
    datetime, timedelta
    
    格式化时间

'''
