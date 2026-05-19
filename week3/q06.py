try:
    num1 = float(input())
    num2 = float(input())
    x = num1 / num2
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(x)