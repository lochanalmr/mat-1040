amount = int(input())

quotient1 = amount // 1000
amount = amount % 1000

quotient2 = amount // 500
amount = amount % 500

quotient3 = amount // 100
amount = amount % 100

quotient4 = amount // 50
amount = amount % 50

quotient5 = amount // 10
amount = amount % 10

print(quotient1)
print(quotient2)
print(quotient3)
print(quotient4)
print(quotient5)