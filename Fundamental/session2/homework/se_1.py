height = int(input("Input your height(cm) = ")) / 100
weight = int(input("Input your weight(kg) = "))

bmi = weight / (height ** 2)
print("BMI = ", bmi)

if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
