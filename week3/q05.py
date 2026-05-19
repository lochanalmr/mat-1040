try:
    number = float(input())
except ValueError:
    print("Invalid input")
else:
    print(number*number)