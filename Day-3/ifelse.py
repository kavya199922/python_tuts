#if conditon:
    # statements
    # ..
# else:
# ..
#conditional statements:direction of execution of code changes based on the condition
balance=1000
withdraw=5000
if withdraw<balance:
    balance=balance-withdraw
    print("success")
else:
    print("amount exceeding balance")

#indentation
#if---elif--else
z=int(input("enter a number"))
if z>5:
    print("greater than 5")#route1
elif z==5:
    print("equal to 5")#rt2
else:
    print("less than 5")#rt3
