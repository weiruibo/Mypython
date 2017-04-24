# coding:utf-8

'''
Created on Apr 22, 2017

@author: weiruibo

    词典 (dictionary) 与列表 (list [] ) 相似，词典也可以储存多个元素。
    这种储存多个元素的对象称为容器(container)。

'''

dic = {'tom':11, 'sam':57, 'lily':100}
print dic
print type(dic)

# 字典没有顺序 不能通过下标引用元素 只能通过键名来引用
a = dic['tom']
print a

dic["sam"] = 120
print dic

# 构建一个新的字典

dic = {}
print dic
dic['lilei'] = 999
print dic

# 循环调用词典元素

#    循环获取键名 再通过字典[键名]来取值



dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}

del dic['tom']  # 删除 dic 的‘tom’元素

print dic 

print len(dic)

for key in dic:
    print "key =", key
    
    print "value =", dic[key]


print dic.keys()  # 返回dic所有的键
print dic.values()  # 返回dic所有的值
print dic.items()  # 返回dic所有的元素（键值对）
dic.clear()  # 清空dic，dict变为{}
print dic

'''
词典的每个元素是键值对。元素没有顺序。

    dic = {'tom':11, 'sam':57,'lily':100}
    
    dic['tom'] = 99
    
    for key in dic: ...
    
    del, len()
    
    del是Python中保留的关键字，用于删除对象。

'''
