import math

def loan_repayment_estimation_cal():
    l = float(input())
    r = (float(input()) / 12) / 100
    n = int(input())
    M = l * r * math.pow((1 + r), n) / (math.pow((1 + r), n) - 1)
    return M

print(loan_repayment_estimation_cal())