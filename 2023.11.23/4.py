coord_1 = input()
coord_2 = input()

coord_1_int = int(coord_1[1])
coord_1_ltr = coord_1[0]
coord_2_int = int(coord_2[1])
coord_2_ltr = coord_2[0]

coord_1_sum = (ord(coord_1_ltr) + int(coord_1_int)) % 2
coord_2_sum = (ord(coord_2_ltr) + int(coord_2_int)) % 2

if (1 <= coord_1_int <= 8 and
    'a' <= coord_1_ltr <= 'h' and
    1 <= coord_2_int <= 8 and
    'a' <= coord_2_ltr <= 'h' and
    coord_1_sum == coord_2_sum):    
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