coord1 = input()
coord2 = input()

coord1_int = int(coord1[1])
coord1_ltr = coord1[0]
coord2_int = int(coord2[1])
coord2_ltr = coord2[0]

if (coord1 != coord2 and
        1 <= coord1_int <= 8 and 'a' <= coord1_ltr <= 'h' and
        1 <= coord2_int <= 8 and 'a' <= coord2_ltr <= 'h' and
        (coord1_int == coord2_int or coord1_ltr == coord2_ltr)):    
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
