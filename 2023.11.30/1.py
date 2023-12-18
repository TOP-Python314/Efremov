a = []
while (num := int(input())) % 7 == 0:
    a.append(num)
else:
    print(*a)
    
# 7
# 14
# 21
# 12
# 7 14 21