#set of statements that performs a specific task
#function definition ,function call
def sample(x,y):
    return x+y,x-y
    # print("inside function", id(x))

x=5
y=10
#print("outside fun:bef call",id(x))
sum,diff=sample(x,y)
print(sum,diff)
# print("outside fun:after call",id(x))
#arg:values that are passed to a function
