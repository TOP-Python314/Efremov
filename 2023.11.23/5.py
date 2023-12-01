coord_1 = input()
coord_2 = input()

coord_1_int = int(coord_1[1])
coord_1_ltr = coord_1[0]
coord_2_int = int(coord_2[1])
coord_2_ltr = coord_2[0]

if (coord_1 != coord_2 and
        1 <= coord_1_int <= 8 and 'a' <= coord_1_ltr <= 'h' and
        1 <= coord_2_int <= 8 and 'a' <= coord_2_ltr <= 'h' and
        (coord_1_int == coord_2_int or coord_1_ltr == coord_2_ltr)):    
    print('да')
else:
    print('нет')
 
# Ввод 1: 
# c3
# c3
# нет

# Ввод 2:
# b2
# f2
# да

# Ввод 3:
# a12
# q12
# нет
