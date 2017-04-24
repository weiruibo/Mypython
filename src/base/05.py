# -*- coding:utf-8 -*-
'''
Created on Apr 21, 2017

@author: weiruibo
                
        if判断选择
        
        缩进与选择
        
        冒号之后四个空格缩进

'''

i = 1
x = 1

if i > 0:    x = x + 1;

if i > 1:
    
     x = x + 1
    
print x

i = 1
if i > 0:
    print 'positive i'
    i += 1
elif i == 0:
    print 'i is 0'
    i *= 10
else:
    print 'negative i'
    i -= 1

print 'new i is', i    

    
i = 5
if i > 1:
    print 'i bigger than 1'
    print "good"
    
    if i > 2:
            print 'i bigger than 2'
            print 'even better'
    
   

'''

        if语句之后的冒号
        
        以四个空格的缩进来表示隶属关系, Python中不能随意缩进
        
        if  <条件1>:
        
            statement
        
        elif <条件2>:
        
            statement
        
        elif <条件3>：
        
            statement
        
        else:
        
            statement
            
'''

