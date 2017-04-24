# coding:utf-8

'''
Created on Apr 22, 2017

@author: weiruibo

    循环对象

'''

f = open('test.txt', 'r')

# print f.next()
# print f.next()
# print f.next()

for line in f:
    print line
    
# open()返回的实际上是一个循环对象 
# 不用在循环还没有开始的时候，就生成好要使用的元素


''' 生成器
     生成器(generator)的主要目的是构成一个用户自定义的循环对象。
'''
    
print 
    
def gen():
    a = 100
    yield a
    
    a *= 8
    
    yield a
    
    yield 1000
    
''' 生成器有几个yield就循环几次 '''
    
for g in gen():
    
    print g
    
def gen2():
    
    for i in range(5):
        yield i

for g in gen2():
    print g
    
    
''' 生成器表达式 '''
    
G = (x for x in range(4))

for i in G :
    print i
    
''' 表推导'''
    
L=[]

for i in range(8):
    
    L.append(i**2)
    
print L

L=[x+2 for x in range(8)]
print L


x1=[1,3,5]
y1=[9,12,13]

L=[x**2 for (x,y) in zip(x1,y1) if y>10]

print L


'''
    循环对象 (open())

    生成器 (自定义的循环对象)
    yield 有几个yield就循环几次
    
    生成器表达式
    G=(x for x in range(10))  
    x相当于yield的元素

    表推导
        快速生成表
    
    L=[x for x in range(3)] 
    >>> [0,1,2]
    

'''


