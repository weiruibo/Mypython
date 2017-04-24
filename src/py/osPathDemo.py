#coding:utf-8
'''
Created on Apr 23, 2017

@author: weiruibo

    路径与文件
'''
import os.path
path='/Users/weiruibo/Desktop/test.txt'

print os.path.basename(path) # 查询路径中包含的文件名
print os.path.dirname(path)  # 查询路径中包含的目录

info =os.path.split(path) # 将路径分割成文件名和目录两个部分，放在一个表中返回
print info

path2=os.path.join('/','Users','weiruibo','Desktop','doc','test.txt') # 使用目录名和文件名构成一个路径字符串
print path2

p_list=[path,path2]

print os.path.commonprefix(p_list)  # 查询多个路径的共同部分
print os.path.normpath(path)


print(os.path.exists(path))    # 查询文件是否存在

print(os.path.getsize(path))   # 查询文件大小
print(os.path.getatime(path))  # 查询文件上一次读取的时间
print(os.path.getmtime(path))  # 查询文件上一次修改的时间

print(os.path.isfile(path))    # 路径是否指向常规文件
print(os.path.isdir(path))     # 路径是否指向目录文件



import glob

print glob.glob("/users/weiruibo/*")  #符合该表达式的文件（与正则表达式类似） 相当于ls
