marks = int(input())
if marks >= 35:
    pass_or_fail = "Pass"
    if marks >= 75:
        grade = "A"
    elif marks >= 65:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "S"
else:
    pass_or_fail = "Fail"
    grade = "F"

print(grade)
print(pass_or_fail)