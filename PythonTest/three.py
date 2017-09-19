#-*- coding:utf-8 -*-

#  添加self作为全局变量
class Student(object):
    def __init__(self):
        self.name = '11'
        self.age = 0
        print (u"答应")
    def getpropty(self):
        print (self.name)

    def getpropty1(self):
        print (self.name)



studeng = Student()
studeng.getpropty()
