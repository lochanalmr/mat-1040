name1 = input()
name2 = input()
score = (len(name1) + len(name2)) % 101

print(score)
if score >= 80:
    print('Excellent match')
elif score >= 50:
    print('Good match')
else:
    print('Needs more understanding')