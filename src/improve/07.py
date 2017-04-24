# coding:utf-8
'''
Created on Apr 22, 2017

@author: weiruibo

        函数对象
        
'''

''' lambda 函数'''
# def func(x, y):
#     return x + y

func = lambda x, y: x + y  # #lambda 后面带参数 冒号后面即返回值 省略return

print func(3, 4)

func2 = lambda :5

print func2

''' 函数作为参数传递 '''


def test(f, a, b):
    print 'test'
    print f(a, b)
    
test(func, 3, 5)

test((lambda x, y: x + y), 6, 9)


'''    map(func,list[]) 函数 
        第一个参数传入函数对象
        第二个参数传入一个多元素的表
        map()的功能是将函数对象依次作用于表的每一个元素
        返回一个表

'''
# 函数对象一个参数
re = map((lambda x: x + 2), [0, 2, 4, 6, 8])

print re

# 函数对象多个参数
# map()将每次从两个表中分别取出一个元素，带入lambda所定义的函数。
re = map((lambda x, y:x + y), [1, 2, 3], [4, 5, 6])
print re

'''
    filter(func,list[])函数
    用于筛选数据
    如果函数对象返回的是True 则将该元素返回到表中
    
'''

def func(a):
    if a>100:
        return True
    else:
        return False

re=filter(func,[99,100,120,150,88])
print re

'''
    reduce(func,list[])函数
    用于累进地将函数作用于各个参数
    
'''

print reduce((lambda x,y:x+y),[1,2,3,4,5])
##>>>(((1+2)+3)+4)+5

# reduce将表中的前两个元素(1和2)传递给lambda函数，得到3。
# 该返回值(3)将作为lambda函数的第一个参数，而表中的下一个元素(4)作为lambda函数的第二个参数，进行下一次的对lambda函数的调用，得到7。
# 依次调用lambda函数，每次lambda函数的第一个参数是上一次运算结果，而第二个参数为表中的下一个元素，直到表中没有剩余元素。

'''
函数是一个对象

用lambda定义函数
    
    只能定义简单函数
    :冒号后面只能有一个表达式

map()
    如果函数对象有多个参数可以有多个表 返回表
    
    作用:简单的数据操作:  + - * /
        将函数依次作用于参数(表中的每个元素)

filter()
    只能有一个函数对象和一个表
    
    作用:数据筛选 只有返回TRUE才将元素返回表
    
reduce()
    只能有一个函数对象和一个表
    
    作用:函数对象的累加元素
        返回数值
    
    
'''
