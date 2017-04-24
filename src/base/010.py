# coding:utf-8

'''
Created on Apr 21, 2017

@author: weiruibo

    
    内置函数
    type() 查看变量类型
    range() 生成一个表
    dir() 查询一个累或者对象的所有属性
    help() 查询说明文档
    
'''

# print type(list)
# print dir(list)
# print help(list)


class Human():
    name = "lilei"
    gender = "man"
    age = 10
    def move(self):
        print "move to school"
        
print type(Human)
print dir(Human)
print help(Human)

# list(表)是一个类 里面有list的方法
# 
# n1就是list的一个对象
n1 = [0, 1, 2, 3, 4, 5]
print type(n1)
print n1.count(4) #计数,看总共有多少个4
print n1.index(3) #查看下标为3的数据
n1.append(4) #在最后添加一个新元素 4
n1.sort() #对n1元素进行排序
print n1

print n1.pop() #去掉最后一个元素 并返回该元素
print n1

n1.remove(4) #除去第一个4
print n1

n1.insert(1,10) #在下标为1的地方插入10
print n1


print dir(list)
print help(list)
print [1,2,3]+[4,5,6]

class superList(list):
    def __sub__(self, b):
        a = self[:]     # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]        
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([3,4])

'''
        len() 用来返回list所包含的元素的总数
        
        type() 查看变量类型
        
        range() 生成一个表
        
        dir() 查询一个累或者对象的所有属性
        
        help() 查询说明文档
        
        数据结构list(列表)是一个类。
        
        运算符是方法
'''