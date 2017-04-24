# coding:utf-8

'''
Created on Apr 22, 2017

@author: weiruibo

        循环设计
'''


str = "abcdefghijk"

# for i in str:
#     print i
    
for i in range(len(str)):
    print str[i]

for i in range(0, len(str), 3):  # 在range()函数中定义 range(上限,下限,步长)
    print str[i]

'''
    通过下标获取元素
'''
    
'''enumerate()函数，可以在每次循环中同时得到下标和元素'''
    
    
for i in enumerate(str): #enumerate返回的是一个元组
    print i

for (k,v) in enumerate(str):
    print k,"->",v
    
    
''' zip()函数的功能，就是从多个列表中，依次各取出一个元素。
    每次取出的(来自不同列表的)元素合成一个元组，合并成的元组放入zip()返回的列表中。
    zip()函数起到了聚合列表的功能。
'''
    
ta = (1,2,3)
tb = [9,8,7]
tc = ['a','b','c']

for i in zip(ta,tb,tc):
    print i
    
for (a,b,c) in zip(ta,tb,tc):
    print a,"->",b,'->',c
    
    
ta=[1,2,3,4]
tb=(9,8,7,5)

zipped=zip(ta,tb)
print zipped

print zip(zipped)

na,nb = zip(*zipped)

print na ,'-->',nb

n=zip(*zipped)
print n
print n[0]
print n[1]


'''

    range(上限,下限,步长) 可以通下标获取元素
        
        for i in range(0, len(str), 1):  # 在range()函数中定义 range(上限,下限,步长)
            print str[i]




    enumerate() 在循环中返回一对元组值(key,value)
    
        for (key,value) in enumerate(str):
            print key
            print value



    zip() 聚合序列
    
        分解聚合后的列表
        
        ta=(1,2,3)
        tb=(4,5,6)
        
        n=zip(ta,tb)
        
        >>> [(1,4),(2,5),(3,6)]
    
        nn=zip(*n)
        
        >>> [(1,2,3),(4,5,6)]
    

'''
