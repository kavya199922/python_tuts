#for:iterate list,tuple,dictionaries
a=[1,2,3]
for x in a:
    print(x)
#dict
d={1:'a',2:'b',3:'c'}
for k in d:
    print(d[k])#d[1],d[2],d[3]
#if
a=[1,2,4,5]
b=[2,3,5,9]
c=[]
for ele in a:
    if ele in b:
        c.append(ele)
print(c)


