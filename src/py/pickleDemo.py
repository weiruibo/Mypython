# coding:utf-8
'''
Created on Apr 23, 2017

@author: weiruibo

    存储对象
    
        存储对象的内容到本地文件中
    
    在之前对Python对象的介绍中 (面向对象的基本概念，面向对象的进一步拓展)，
    我提到过Python“一切皆对象”的哲学，在Python中，无论是变量还是函数，都是一个对象。
    当Python运行时，对象存储在内存中，随时等待系统的调用。
    然而，内存里的数据会随着计算机关机和消失，如何将对象保存到文件，并储存在硬盘上呢？

    计算机的内存中存储的是二进制的序列 (当然，在Linux眼中，是文本流)。
    我们可以直接将某个对象所对应位置的数据抓取下来，转换成文本流 (这个过程叫做serialize)，然后将文本流存入到文件中。
    由于Python在创建对象时，要参考对象的类定义，所以当我们从文本中读取对象时，
    必须在手边要有该对象的类定义，才能懂得如何去重建这一对象。
    从文件读取时，对于Python的内建(built-in)对象 (比如说整数、词典、表等等)，由于其类定义已经载入内存，
    所以不需要我们再在程序中定义类。但对于用户自行定义的对象，就必须要先定义类，
    然后才能从文件中载入对象 (比如面向对象的基本概念中的对象那个summer)。
'''
import pickle


class Bird(object):
    
    have_feather=True
    way_of_reproduction='egg'
    
    
summer=Bird()

p=pickle.dumps(summer)
print p

f=open('/Users/weiruibo/Desktop/hello.py','w')
f.write(p)
f.flush()
f.close()

# f=open('/Users/weiruibo/Desktop/hello.py','r')
# str=""
# for i in f:
#    str+i
#    
# print str
# 
# summer=pickle.load(str)

with open('/Users/weiruibo/Desktop/hello.py','r') as f:
    a=pickle.load(f)

print a.have_feather

'''
Python/Java里面，对象必须经过序列化，才能存储。

'''
