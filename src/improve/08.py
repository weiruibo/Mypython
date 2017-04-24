#coding:utf-8
'''
Created on Apr 22, 2017

@author: weiruibo

    异常处理
    
'''


re = iter(range(5))

try:
    for i in range(100):
        print re.next()

except:
    print 'here is a problem',i
print 'HaHaHaHa'

try:
    print(a*2)
except TypeError:
    print("TypeError")
except:
    print("Not Type Error & Error noted")
    
    
def test_func():
    try:
        m = 1/0
    except NameError:
        print("Catch NameError in the sub-function")

try:
    test_func()
except ZeroDivisionError:
    print("Catch error in the main program")
    
    
print 'Lalala'
raise StopIteration
print 'Hahaha'


'''


try->异常->except->finally

try->无异常->else->finally

try: ... except exception: ... else: ... finally: ...
raise exception

raise 用于抛出异常
'''