weight = float(input("weight(kg):"))
height = float(input("height(cm): "))








height /= 100
z = float(weight / (height ** 2))
z = round(z,1)

if z >= 35 and z <= 39.9:
    print("Your BMI is ",z," «Extreme Obesity»")

elif z >= 30 and z <= 34.9:
    print("Your BMI is ",z," «Obesity»")

elif z >= 25 and z <= 29.9:
    print("Your BMI is ",z," «Overweight» ")

elif z >= 18.5 and z <= 24.9:
    print("Your BMI is ",z," «Normal Weight:)")

else:
    print("Your BMI is ",z," «Underweight")