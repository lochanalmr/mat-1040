units = float(input())

if units <= 60:
    price = 250 + units * 25

elif units <= 90:
    price = 400 + 60 * 25
    price = price + (units - 60) * 35

else:
    price = 700 + 60 * 25
    price = price + 30 * 35
    price = price + (units - 90) * 50

print(price)