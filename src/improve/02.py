# coding:utf-8

'''
Created on Apr 22, 2017

@author: weiruibo

        文本文件的输入输出
        通过内置函数open()构建的对象来操作
        
'''

f=open("01.py") ##不加模式时默认为只读
print f
print "-------------------------------"

content=f.read(9)  # 读取N bytes的数据
print content

print "-------------------------------"
content=f.readline() # 读取一行
print content

print "-------------------------------"
content=f.readlines() # 读取所有行，储存在列表中，每个元素是一行。
print content[1]

f.close()

f=open("record.txt",'w')
f.write("tom, 12, 86 \nLee, 15, 99 \nLucy, 11, 58 \nJoseph, 19, 56")

f.close()


f=open("record.txt")
content=f.readlines()


for i in content:
    print i
    
f.close()

ff=open("record.txt","w")
ff.write("hello world")
ff.close();

f=open("record.txt")
content=f.readlines()


for i in content:
    print i
    
f.close()

'''

        f    = open(name, "r")
        
        line = f.readline()
        
        f.write('abc')
        
        f.close()
        
        对于open()对象每次只能操作一种模式,即读不能写,写不能读 

'''


    


