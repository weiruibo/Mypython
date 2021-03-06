#coding:utf-8
'''
Created on Apr 23, 2017

@author: weiruibo

    文件管理
    
    
    os包包括各种各样的函数，以实现操作系统的许多功能。这个包非常庞杂。os包的一些命令就是用于文件管理。我们这里列出最常用的:

    mkdir(path)
    
    创建新目录，path为一个字符串，表示新目录的路径。相当于$mkdir命令
    
    rmdir(path)
    
    删除空的目录，path为一个字符串，表示想要删除的目录的路径。相当于$rmdir命令
    
    listdir(path)
    
    返回目录中所有文件。相当于$ls命令。
    
     
    
    remove(path)
    
    删除path指向的文件。
    
    rename(src, dst)
    
    重命名文件，src和dst为两个路径，分别表示重命名之前和之后的路径。 
    
     
    
    chmod(path, mode)
    
    改变path指向的文件的权限。相当于$chmod命令。
    
    chown(path, uid, gid)
    
    改变path所指向文件的拥有者和拥有组。相当于$chown命令。
    
    stat(path)
    
    查看path所指向文件的附加信息，相当于$ls -l命令。
    
    symlink(src, dst)
    
    为文件dst创建软链接，src为软链接文件的路径。相当于$ln -s命令。
    
     
    
    getcwd()
    
    查询当前工作路径 (cwd, current working directory)，相当于$pwd命令。
    
     
    
    比如说我们要新建目录new：
    
    import os
    os.mkdir('/home/vamei/new')
'''
import os
import shutil

#os.rmdir('/Users/weiruibo/Desktop/w')

print os.listdir('/Users/weiruibo')
print os.stat("/Users/weiruibo")

'''
copy(src, dst)

复制文件，从src到dst。相当于$cp命令。

move(src, dst)

移动文件，从src到dst。相当于$mv命令。

 

比如我们想复制文件a.txt:

'''

# os.mkdir('/Users/weiruibo/Desktop/pytest')

shutil.copy('/Users/weiruibo/Desktop/test.png', '/Users/weiruibo/Desktop/pytest/test1.png')

shutil.move('/Users/weiruibo/Desktop/test.png', '/Users/weiruibo/Desktop/test1.png')
