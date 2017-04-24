# coding:utf-8
'''
Created on Apr 22, 2017

@author: weiruibo

        函数的参数对应
    
'''

# # 位置传递
def f(a, b, c):
    return a + b + c
print f(1, 2, 3)

# #关键字传递

print f(a=10, b=20, c=5)


# #位置 关键字混合
# # 位置参数一定要在关键字参数前面

print f(10, b=2, c=3)


# #默认参数

def ff(a, b, c=100):
    return a + b + c
print ff(2, 3)
print ff(2, 3, 50)


'''

    包裹传递

        在定义函数时，我们有时候并不知道调用的时候会传递多少个参数。
        这时候，包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会非常有用。

'''
# #包裹位置传递
# #所有参数被name收集,根据位置合并成一个元组
# #name是包裹位置传递所用的元组名,在定义时在name前面加*号

def func(*name):
    print type(name)
    print name
    
func(1, 2, 4)
func(5, 6, 7, 10, 2)



# #包裹关键字传递

# #dict是一个字典 所有参数被dict收集

# #dict是包裹关键字传递的字典名,在定义是在dict浅加**号

def func2(**dict):
    print type(dict)
    print dict
    
func2(a=1, b=9)
func2(m=1, n=2, k=100)

'''

        包裹传递的关键在于定义函数时，在相应元组或字典前加*或**。

'''

'''

    解包裹

'''


# 就是在传递tuple时，让tuple的每一个元素对应一个位置参数
# 在传入参数前面加上*
def func3(a, b, c):
    print a, b, c
    print a + b + c

args = (4, 5, 6)
func3(*args)


# 在传递词典dict时，让词典的每个键值对作为一个关键字传递给func。
# 在传入参数前面加上**
dict = {"a":1, "b":100, "c":20}

func3(**dict) ##得到value
func3(*dict) ##得到key


'''
        在定义或者调用参数时，参数的几种传递方式可以混合。
        但在过程中要小心前后顺序。
        基本原则是，先位置，再关键字，再包裹位置，再包裹关键字
        
         
        
        注意：请注意定义时和调用时的区分。包裹和解包裹并不是相反操作，是两个相对独立的过程。
        
        关键字，默认值，

        包裹位置，包裹关键字
        
        解包裹

'''
