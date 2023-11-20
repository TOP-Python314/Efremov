num = str(input())
mult = 1
for i in num:
    mult *= int(i)
print(sum([int(i) for i in num]))
print(mult)
