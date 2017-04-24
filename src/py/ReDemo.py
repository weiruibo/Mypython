#coding:utf-8
'''
Created on Apr 22, 2017

@author: weiruibo

     标准库1 re包
'''

import re

str="asdf1231as"

m=re.search('[\d]{3}',str)
print type(m)
print m.group(0)

m=re.match('[\d]',str)
print m
'''
    m = re.search(pattern, string)  # 搜索整个字符串，直到发现符合的子字符串。
    m = re.match(pattern, string)   # 从头开始检查字符串是否符合正则表达式。必须从字符串的第一个字符开始就相符。

'''


# 在string中利用正则变换pattern进行搜索，对于搜索到的字符串，用另一字符串replacement替换。返回替换后的字符串。
mm=re.sub('[\d]'," weiruibo ",str)
print mm


#re.split()    # 根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回

# re.findall()  # 根据正则表达式搜索字符串，将所有符合的子字符串放在一给表(list)中返回


m = re.search("output_(\d{4})", "output_1986.txt")
print(m.group(1))

m = re.search("output_(\d)(\d)(\d)(\d)", "output_1986.txt")
print(m.group(3))

m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
print(m.group("year"))

'''
有一个文件，文件名为output_1981.10.21.txt 。
下面使用Python： 读取文件名中的日期时间信息，并找出这一天是周几。
将文件改名为output_YYYY-MM-DD-W.txt (YYYY:四位的年，MM：两位的月份，DD：两位的日，W：一位的周几，并假设周一为一周第一天)
'''

str="output_1981.10.21.txt"

m=re.search('(?P<year>[\d]{4}).(?P<mon>[\d]{2}).(?P<day>[\d]{2})',str)
y=m.group("year")
mon=m.group("mon")
d=m.group("day")



