# coding:utf-8
'''
Created on Apr 22, 2017

@author: weiruibo

    模块
    在Python中，一个.py文件就构成一个模块。通过模块，你可以调用其它文件中的程序。

'''

import first


# for i in range(8):
first.laugh()
     

# 通过 模块.对象 的方式来调用引入模块中的某个对象

import first as second  # 引入模块first，并将模块a重命名为second

print second.hh  

from first import laugh #从模块first中引入laugh对象。
                        # 调用fisrt中对象时，我们不用再说明模块，即直接使用laugh，
                        #而不是first.laugh
laugh()


from first import * #从模块first中引入所有对象。

print hh



