n = int(input())
if n == 1:
    print(1)
elif n % 2 == 0:
    print(sum(i for i in range(2, n//2 + 1) if n % i == 0) + 1 + n)
else:
    print(sum(i for i in range(3, n//3 + 1) if n % i == 0) + 1 + n)
    
# Ввод 1:
# 146
# 222

# Ввод 2:
# 81
# 121