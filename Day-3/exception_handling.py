a=5
b=0
# print(a/b)
# print("bye")
#divide
try:
    print("program starts")
    c = int(input("enter a number"))#w
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e1:
    print(e1)
except Exception as e2:
    print(e2)
finally:
    print("program stopped")
