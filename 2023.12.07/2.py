fruits_list = []
while True:
    fruit = input()
    if fruit != '':
        fruits_list.append(fruit)
    else:
        if len(fruits_list) == 1:
            print(*fruits_list)
        elif len(fruits_list) == 2:
            print(*fruits_list, sep=' и ')
        else:
            print(*fruits_list[:-1], sep=', ', end=' и ')
            print(fruits_list[-1])
        break

# Ввод 1:
    # авокадо
    # грейпфрут
    # дыня
    # банан
    # ананас

    # авокадо, грейпфрут, дыня, банан и ананас

# Ввод 2:
    # киви
    # груша

    # киви и груша  

# Ввод 3:
    # лайм

    # лайм