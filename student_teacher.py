#!/usr/bin/env python3
class Person(object):
    '''
    fan hui gei ding ming cheng de Person duixiang
    '''
    def __init__(self,name):
        self.name = name
    def get_details(self):
        return self.name

class Student(Person):
    '''
    fanhui Student duixiang,caiyong name branch year 3 ge canshu
    '''
    def __init__(self,name,branch,year):
        Person.__init__(self,name)
        self.branch = branch
        self.year = year
    def get_details(self):
        return "{} studies {} and is in {} yaer.".format(self.name,self.branch,self.year)

class Teacher(Person):
    def __init__(self,name,papers):
        Person.__init__(self,name)
        self.papers = papers
    def get_details(self):
        return "{} teaches {}.".format(self.name,self.papers)

person1 = Person('bob')
student1 = Student('kas','jds',2001)
teacher1 = Teacher('jkds',['python','c++'])
print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
