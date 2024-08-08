# Calculator for basic arithmetic operations
#Input from the user
a = float(input("enter the First number:\n"))
b = float(input("enter the Second number:\n"))
c = input("Select operation ->> +,-,*,/,^ \n")
#Operations
if c == "+" :
    print(a, "+", b,"=",a+b)
elif c == "-":
    print(a, "-", b,"=",a-b)
elif c == "*":
    print(a, "*", b,"=",a*b)
elif c == "/":
    if b == 0.0 :
        print("Error of 0")
    else:
        print(a, "/", b,"=",a/b)
elif c == "^":
    print(a, "^", b,"=",a**b)
else:
    print("Error")        

