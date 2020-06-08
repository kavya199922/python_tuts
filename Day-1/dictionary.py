#key-value pairs
#{key:value,}
dict1={1:['a','x','y'],2:'b',3:'c'}
#change the value
#dict1[1]='z'
print(dict1)
print(dict1.values())
#get
print(dict1.get(10,"no key found"))
#pop
print(dict1.popitem())
print(dict1)
print(type(dict1))
dict2=dict(name='kavya',age=21)
print(dict2)
#update
d={'name':'kavya','age':21}
d.update({'city':'chennai'})
print(d)
x=[1,2,3]
y=['a','b','c']
print(dict(zip(x,y)))
