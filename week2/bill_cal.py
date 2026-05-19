bill = float(input())
if bill < 5000:
    discount = 0

elif bill < 10000:
    discount = bill * 0.05
    bill = bill * 0.95

elif bill < 20000:
    discount = bill * 0.1
    bill = bill * 0.9

else:
    discount = bill * 0.15
    bill = bill * 0.85

print(f"${discount}")
print(f"${bill}")