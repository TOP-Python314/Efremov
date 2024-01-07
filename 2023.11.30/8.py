n = int(input())

num1 = 1
num2 = 1

for i in range(n):
    print(num1, end=' ')
    num1, num2 = num2, num1 + num2
    
# 21
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946