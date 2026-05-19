age = int(input())
if age < 5:
    print('Free')
    price = 0
elif age <= 12:
    print('Child')
    price = 400
elif age <= 59:
    print('Adult')
    price = 800
else:
    print('Senior')
    price = 500

print(price)