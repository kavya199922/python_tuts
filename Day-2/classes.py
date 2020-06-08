#class:pre-defined;user-defined
class Employee:
    companyname='xyz'
    #constructor:
    def __init__(self):
        print("it's a constructor")
    def fun1(self,name,age):#self:object
        self.name=name
        self.age=age
        print("this is fun1")
e1=Employee()#object:instance
print(e1.companyname)
e2=Employee()
print(e2.fun1('Eric',21))
print(e2.name)
#inheritance:reusability:
class Parent:
    def fun2(self):
        print("Inside Parent")
class Child(Parent):
    def fun3(self):
        print("Inside child")
c=Child()
c.fun3()
c.fun2()