# -*- coding: utf-8 -*-
'''
Created on Apr 21, 2017

@author: weiruibo

    sequence序列
    
        有顺序的元素集合(对象的集合)
        
        可以是一个或多个元素,也可以没有元素 (元素即基本数据类型)
        
        tuple(元组 用()表示) list(表 用[]表示)

'''

s1 = (2, 1.3, False, "Hello", 6.5, 20, 37, True)
s2 = [24, 2.5, True, "World"]
print s1
print type(s1)
print 
print s2
print type(s2)

# 区别 tuple()中的元素不能改变 list[] 中的元素可以改变


# #一个序列可以作为另一个序列的元素
s3 = [1, [3, 4, 5]]
print s3

s4 = []
##s4[2]=100
s4.append(2)
print "s4 =",s4


print "s1[0] =", s1[0]
print "s2[2] =", s2[2]
print "s3[1] =", s3[1]

ss = s3[1]
print ss[2]

s2[2] = 5.0
print "s2[2] =", s2[2]


# #基本样式[下限:上限:步长]
print ("基本样式[下限:上限:步长]")

print "s1=", s1
# print "s2=", s2

"""
    s1= (2, 1.3, False, 'Hello', 6.5, 20, 37, True)
"""

print "s1[5] =", s1[5]
print "s1[:5] =", s1[:5], "    ##从0下标到下标4 下标5的元素不包括在内"
print "s1[2:] =", s1[2:], "    ##下标2到最后"
print "s1[0:5:2] =", s1[0:5:2], "    ##下标0到4 每隔2个元素取一个元素 即下标为0,2,4"
print "s1[0:2] =", s1[0:2], "    ##下标0到1"
print "s1[2:0:-1] =" , s1[2:0:-1],"    ##下标2到下标1"

print "s1[-1] =", s1[-1], "    ##倒数第一个"
print "s1[-3] =", s1[-3], "    ##倒数第三个"
print "s1[0:-1] =", s1[0:-1], "    ##第一个到倒数第二个"

print "s2=",s2[:]

# 字符串也是一种特殊的元元组
str = "hello world"
print str[1:5]
print type(str)

'''
    tuple元素不可变，list元素可变
    
     基本样式[下限:上限:步长]
    
    序列的引用 s[2], s[1:8:2]
    
    字符串也是一种特殊的元组
    
    空序列赋值需要调用序列的append()方法 不能直接使用 序列[下标] 赋值
    
    步长-1代表 从右到左 默认为从左到右
'''

