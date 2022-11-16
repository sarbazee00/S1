import math

print ("super calculator")



print ("+   -   *  /")
print ("sin cos  tan cot")
print ("factorial   sqrt")
print ("log    **    x^2")

op = input("please enter your choice")

if op == "+" or op == "-" or op == "*" or op == "/" or op == "**" :
    a=float (input("numer1:"))
    b=float (input("number2:"))

if op == "sin" or op == "cot" or op == "tan" or op == "cos" or op == "*factorial"or op == "sqrt" or op == "log" or op == "x^2" :
    a=float (input("numer1:"))

if op == "+":
    z=a+b
if op == "-":
    z =a-b
if op == "*":
    z =a*b
if op == "/":
    if b==0:
        z = "EROE=TN"

    else :
        z =a/b

if op == "sin":
    z=math.sin(a)

if op == "cos":
    z=math.cos(a)

if op == "tan":
    z=math.tan(a)

if op == "cot":
    z=1/(math.tan(a))

if op == "factorial":
    z=math.factorial(a)

if op == "log":
    z=math.log(a)

if op == "x^2":
    z=a**2

if op == "**":
    z=a**b






print(z)