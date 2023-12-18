n = int(input())

num_1 = 1
num_2 = 1

for i in range(n):
    print(num_1, end=' ')
    num_1, num_2 = num_2, num_1 + num_2
    
# 21
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946