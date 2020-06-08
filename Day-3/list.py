#list:heterogenous
list1=[1,2,3,'a',6.7]
print(type(list1))
#1 2 3 a 6.7
#0 1 2 3 4
print(list1[0])
#add
#append
list1.append(33)
print(list1)
list1.insert(0,21)
print(list1)
#extend
# list1.extend((34,"hello",98))
# print(list1)
# list2=[*list1,56]
# print(list2)
#listof list
# list3=[25,"thursday",['a','b','c']]
# print(list3[2][0])
# list4=list3.copy()
# print(list4)
#pop
print(list1.pop())
#remove
list1.remove(21)
print(list1)
a=[1,24,66,501,24]
a[0]=1.5
print((a))
print(a.count(24))
#tuple->immutable
tuple1=(1,24,5)
#set->unique
#set1={1,2,3}
#set1=set([66,24,66,90])
#print(set1)
set1={1,2,3,4,5}
#print(set1)
set2={2,3,6,7,5}
print(set1.intersection(set2))
#setname.update()
set1.discard(51)
print(set1)
#frozenset
a=frozenset([23,45,66])
#a.add(34)
l1=[5,4,67]
x,y,z=l1
print(x,y,z)
print(sorted(l1,reverse=True))
print(l1)
t1=(1,2,[3,4])
t1[2][1]=7
print(t1)