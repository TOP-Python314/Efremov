coord1 = input()
coord2 = input()

coord1_int = int(coord1[1])
coord1_ltr = coord1[0]
coord2_int = int(coord2[1])
coord2_ltr = coord2[0]

coord1_sum = (ord(coord1_ltr) + int(coord1_int)) % 2
coord2_sum = (ord(coord2_ltr) + int(coord2_int)) % 2

if (1 <= coord1_int <= 8 and
    'a' <= coord1_ltr <= 'h' and
    1 <= coord2_int <= 8 and
    'a' <= coord2_ltr <= 'h' and
    coord1_sum == coord2_sum):    
    print('да')
else:
    print('нет')

# Ввод 1:
# v3
# b4
# нет

# Ввод 2:
# q6
# f3
# нет

# Ввод 3:
# b3
# e4
# да