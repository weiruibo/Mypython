# coding:utf-8
'''
Created on Apr 21, 2017

@author: weiruibo

    for循环
    
'''

#for 元素 in 序列: 
#     statement

for i in [1,2,3,4,"love","H","e",'l','l','o']:
    print i
    
#range()函数用于建表 
list=range(5)   #从0开始建立一个5个数的表 从0开始，下一个元素比前一个大1， 直到函数中所写的上限 （不包括该上限本身）

print list

for a in range(10):
    print a,"** 2 =",a**2

#while
i=0;
while i<10:
    print i;
    i+=1
    
# continue   # 在循环的某一次执行中，如果遇到continue, 那么跳过这一次执行，进行下一次的操作
# 
# break      # 停止执行整个循环

print "-----------------"

for i in range(10):
    if(i==2):
        continue
    if(i==8):
        break;
    print i
    
r=range(0,5)
print type(list)
    
    