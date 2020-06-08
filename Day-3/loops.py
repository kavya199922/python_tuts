#a set of statements are executed continuosly
#stops when the looping condition becomes false
# i=5
# while i<10:#test expression/looping condition:i<10
#     print(i)
#     i=i+1
# #if else can also be present inside loop
# i=1
# while i<10:
#     if i%2==0:
#         print("even:" ,i)
#     else:
#         print("odd: ",i)
#     i=i+1
#infinite loop
# i=1
# while i<=10:
#     print(i)
#     i=i+1
#for loop:iterating/traversing a list,string,tuple,dictionary
# l1=[1,2,3,4]
# for i in l1:#1 2  3 4
#     print(i)
# t1=(1,2,3)
# for i in t1:
#     print(i)
set1={22,44,44,66}
for i in set1:
    print(i)
d={'jonas':'90','adam':'95','magnus':'29'}
# for k,v in d.items():
#     print(f"Key is {k} and value is {v}")
for k in d:
    print(k,d[k])
#range:(1,10):print multiples of 3
for i in range(1,10,1):
    if i%3==0:
        print(i)
a=[1,2,3,4]

b=[5,6,7,8,1,2,3]
new_list = []
for element in a:
    if element in b:
        new_list.append(element)
print(new_list)