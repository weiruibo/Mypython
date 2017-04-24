# coding:utf-8
'''
Created on Apr 21, 2017

@author: weiruibo

        面向对象
'''

class Bird(object):
    have_feather = True
    way_of_reproduction = 'egg'
    
    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx;
        position[1] = position[1] + dy;
        return position

summer = Bird();  # #对象->summer
print summer.way_of_reproduction  # #对对象中属性的引用 对象.属性

print 'after move:', summer.move(5, 8)

'''
        子类
        继承
        
'''

class Chicken(Bird):
    way_of_move = "walk"
    possible_in_KFC = True
    
class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False
    
summer = Chicken();

print summer.have_feather
print summer.move(5, 8)
print summer.way_of_move

'''

子类能使用父类中的属性和方法

    将东西根据属性归类 ( 将object归为class )
    
    方法是一种属性，表示动作
    
    用继承来说明父类-子类关系。子类自动具有父类的所有属性。
    
    self代表了根据类定义而创建的对象。
    
    建立对一个对象： 对象名 = 类名()
    
    引用对象的属性： object.attribute
    
    类中的方法第一个参数必须是调用该方法的对象本身 一般习惯用self

'''

'''
    面向对象进阶

'''
    
class Human(object):    
    
    laugh = 'hahahaah'
    
    def show_laugh(this):
        print this.laugh
    
    def laugh_100th(self):
        for i in range(5):
            self.show_laugh()

lilei = Human()
# lilei.laugh = '666'
lilei.laugh_100th()


'''
    __init__()是一个特殊的方法
    当类中class有__init__()方法时 创建对象是会自动调用这个方法->初始化

'''

class happyBird(Bird):
    def __init__(self, more_words):
        print 'We are happy bird.', more_words
        

summer = happyBird("Happy!")

'''

    如果__init__()方法中有参数时 创建对象是需要传入参数!!!

'''


class man(object):
    
    def __init__(self,input_gender):
        self.gender=input_gender  ##对象的属性 不需要在类定义时先定义
    def printGender(self):
        print self.gender
        
li_lei=man("male")
print li_lei.gender;
li_lei.printGender();



'''
        通过self调用类属性 self.属性名
        
        __init__(): 在建立对象时自动执行
        如果__init__()方法中有参数时 创建对象是需要传入参数!!!
        
        类属性和对象的性质的区别
        
        类属性:
            在定义类(class)时 定义
        对象的属性:
            在初始化时(__init__())时通过self.属性名直接使用

'''


class Human2(object):
    Can_Talk = True
    Can_Walk = True
    Age = 0
    
    gender="man"
    
    Name = ["Li", "Lei"]
 
 
a = Human2()
b = Human2()
 
a.Age += 1
print a.Age
print b.Age
 
a.gender="male"
print a.gender
print b.gender


a.Name[0] = "Wang"
print a.Name
print b.Name

'''
    对于基本数据类型 (整数,字符串)在修改对象的属性是不会影响到原来类中的属性
    如果修改的是序列 如 元组或者表事 会影响到原来类中的数据

'''
