#coding:utf-8
'''
Created on Apr 22, 2017

@author: weiruibo

    动态类型
    
'''

a = 3
a = 'at'

''' 对象 3 通过 a 引用 (引用a指向对象3)'''
''' 引用a指向 字符串'at' python会将没有引用指向的对象销毁    '''

a = 5
b = a  #''' b = a的含义是让引用b指向引用a所指的那一个对象 ''' 
a = a + 2

''' 即使是多个引用指向同一个对象，如果一个引用值发生变化，那么实际上是让这个引用指向一个新的引用，并不影响其他的引用的指向 '''

L1 = [1,2,3]
L2 = L1
L1 = 1

print L1
print L2

L1 = [1,2,3]
L2 = L1
L1[0] = 10
print L1
print L2


''' 因为L1，L2的指向没有发生变化，依然指向那个表。
    改变的是表的元素 而不是指向

表实际上是包含了多个引用的对象 '''


def f(x):
    x = 100
    print x

a = 1
f(a)
print a

def ff(x):
    x[0] = 100
    print x

a = [1,2,3]
ff(a)
print a


'''
引用和对象的分离，对象是内存中储存数据的实体，引用指向对象。

可变对象
   :改变对象自身(in-place change)
    :可变数据对象(mutable object)
        列表 词典
            
不可变对象
    :不能改变对象本身，只能改变引用的指向
    :不可变数据对象(immutable object)
        数字 字符串 元组

函数值传递
    
'''