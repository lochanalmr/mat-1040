import math

def kinetic_energy():
    m = float(input())
    v = float(input())
    return 1/2 * m * math.pow(v, 2)

print(kinetic_energy())