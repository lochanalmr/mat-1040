def simple_interest_calculator():
    p = float(input())
    r = float(input())
    t = float(input())
    interest = p * r * t / 100
    return interest

print(simple_interest_calculator())