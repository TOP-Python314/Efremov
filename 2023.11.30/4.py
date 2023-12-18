n = int(input())
a = 0
if n == 1: # Прибавляет 1, если список состоит из цифр, т.к. 2 не входит в список проверки.
    a += 1
for i in range(10**(n) - 1, 10**(n-1), -2):
    div_check = 0
    for j in range(1, i+1, 2):
        if i % j == 0:
            div_check += 1
    if div_check < 3:
        a += 1
print(a)

# Ввод 1:
# 1
# 4

# Ввод 2:
# 4
# 1061