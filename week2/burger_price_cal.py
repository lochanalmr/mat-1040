burger = input()
mushroom = input()
cheese = input()

def mushroom_add(price, burger):    
    if mushroom == "Y":
        if burger == "M" or burger == "N":
            return price + 1
        elif burger == "L":
            return price + 2
    else:
        return price

    
def cheese_add(cheese, price):
    if cheese == "Y":
        return price + 1
    else:
        return price

if burger == "M":
    price = 5

elif burger == "N":
    price = 8

elif burger == "L":
    price = 10

price = mushroom_add(price, burger)
price = cheese_add(cheese, price)
print(f"${price}")