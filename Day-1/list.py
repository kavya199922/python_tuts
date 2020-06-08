#collection of data(heterogenous)
list1=[1,2,3,"hello",7.8]
print(type(list1))
#list
#add
#append:end
list1.append(51)
print(list1)
#access:index
list2=[1,2,3,55,89,90]
#1->0 2->1 3->2
# -3      -2     -1
print(list2[-1])
#slice operator 1,2,3,55,89,90
print(list2[1:-1])
#slice [start(include):end(exclude)]
#list
list3=['a','b','c',1,2]
list3.clear()
print(list3)
#del
del list3
#print(list3)
#extend,copy
a=[22,33,44]
b=a.copy()
print(b)
a.extend([55,100,99])
print(a)
#insert
a.insert(1,990)
print(a)
#min,max,sum
x=[10,20,30,5,2,150,3,10]
print(sum(x))
#sort,sorted
#x.sort()
print(sorted(x,reverse=True))
print(x)
#count
print(x.count(10))

