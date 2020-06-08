#objects,classes
#class:user-defined data type
#int,float:
print(type(5))
#class:attributes(variables) and methods(operations)
# class classname:
#     attributes
#     methods
#object:instance of a class
class Employee:
    companyname='XYZ'
    def __init__(self):
        print("this is a constructor")
    def add(self,name,age,salary):#self specifies the object whicj is calling it
        self.name=name
        self.age=age
        self.salary=salary




# e1=Employee()#instantiation
# e1.add('Eric',21,25000)
# print(e1.name,e1.age,e1.salary)
#
# print(e1.companyname)

#inheritance
class Parent:
    def __init__(self):
        print("this is a parent constructor")
    def fun1(self):
        print("this is a parent function")
class Child(Parent):
    def __init__(self):
        print("this is a child class")
        super().__init__()
        #Parent:Super class,child:Subclass
    def fun2(self):
        print("this is a child function")

child1=Child()
child1.fun2()
child1.fun1()
a=[1,2,3]
i=0
while i<len(a) :
    print(a[i])
    i+=1
