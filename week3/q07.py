units = int(input())
if units <= 20:
    price = 300 + units * 30
    category = "Low"
elif units <= 40:
    price = 300 + 30 * 20 + (units - 20) * 45
    category = "Medium"
else:
    price = 300 + 30 * 20 + 45 * 20 + (units - 40) * 70
    category = "High"

print(price)
print(category)