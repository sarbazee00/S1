a = input("first name and last name: ")


b = float(input("Enter the first grade: "))
c = float(input("Enter the second grade: "))
d = float(input("Enter the third grade: "))

z = ((b + c + d)/3)

if z >= 17:
    print(a,"Great:)")
elif z >= 12:
    print(a,"Normal")
else:
    print(a,"Fail")