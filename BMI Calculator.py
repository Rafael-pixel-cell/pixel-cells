print("BMI calculator")
print("Please enter your weight")
myWeight = float(input())
print("PLease enter your height")
myHeight = float(input())
myBMI = myWeight / (myHeight/100)**2
print (round(myBMI, 1))
if myBMI<18.5:
    print("Underweight")
elif myBMI>=18.5 and myBMI<=24.9:
    print("normal weight")
elif myBMI>=25.0 and myBMI<=29.9:
    print("Overweight")
elif myBMI>=30.0 and myBMI<=34.9:
    print("Obesity class 1")
elif myBMI>=35.0 and myBMI<=39.9:
    print("Obesity class 2")
else:
    print("Obesity class 3")
