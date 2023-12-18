ticket_num = input()

n1 = sum(int(i) for i in ticket_num[0:3])
n2 = sum(int(i) for i in ticket_num[3:6])

if n1 == n2:
    print('да')
else:
    print('нет')
    
# Ввод 1:
# 903157
# нет

# Ввод 2:
# 372516
# да