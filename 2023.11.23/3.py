year_num = int(input())

if year_num % 400 == 0 or year_num % 4 == 0 and year_num % 100 != 0:
    print('да')
else:
    print('нет')
    
# Ввод 1: 
# 2013
# нет

# Ввод 2:
# 1600
# да

# Ввод 3:
# 1964
# да