# coding:utf-8
'''
Created on Apr 21, 2017

@author: weiruibo

    函数
    
'''

def square_sum(a, b):
    c = a ** 2 + b ** 2
    
    return c  # 返回c的值，也就是输出的功能。Python的函数允许不返回值，也就是不用return。

def test(a, b):
    c = a + b;
    return (a, b, c)

'''
        return可以返回多个值，以逗号分隔。相当于返回一个tuple(定值表)。

        return a,b,c          # 相当于 return (a,b,c)
        
        在Python中，当程序执行到return的时候，程序将停止执行函数内余下的语句。
        
        return并不是必须的，当没有return, 或者return后面没有返回值时，函数将自动返回None。
        
        None是Python中的一个特别的数据类型，用来表示什么都没有，相当于C中的NULL。
        
        None多用于关键字参数传递的默认值。
        
'''

print square_sum(2, 2)

print test(5, 6)

a = 1

def change_integer(a):
    a = a + 1
    return a

print change_integer(a)
print a

#===(Python中 "#" 后面跟的内容是注释，不执行 )

b = [1, 2, 3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print change_list(b)
print b

# 第一个例子，我们将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化。
# 
# 第二个例子，我们将一个表传递给函数，函数进行操作，原来的表b发生变化。


'''
    对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，
    从而不影响原来的变量。（我们称此为值传递）
    
    但是对于表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，
    在函数中对表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递）
    
    在函数中如果没有 return 打印函数(print)得出的结果是None
    
    基本数据类型的参数：值传递

    表作为参数：指针传递
'''


#写一个判断闰年的函数，参数为年、月、日。若是是闰年，返回True


def isRunNian(y,m,d):
    if (y%4==0 and y%100!=0) or y%400==0:
        return True
    else:
        return False

print isRunNian(2010,1,2)

# 普通年能被4整除且不能被100整除的为闰年。（如2004年就是闰年,1901年不是闰年）
# 世纪年能被400整除的是闰年。
