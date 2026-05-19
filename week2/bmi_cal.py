w = float(input())
h = float(input())
bmi = w / (h*h)
print(bmi)

if bmi < 18.5:
    print('Underweight')
elif bmi < 25.0:
    print('Normal weight')
elif bmi < 30.0:
    print('Overweight')
elif bmi < 35.0:
    print('Obese')       