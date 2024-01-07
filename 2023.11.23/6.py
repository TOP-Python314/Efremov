coord1 = input()
coord2 = input()

coord1_int = int(coord1[1])
coord1_ltr = coord1[0]
coord2_int = int(coord2[1])
coord2_ltr = coord2[0]

if (coord1 != coord2 and
        1 <= coord1_int <= 8 and 'a' <= coord1_ltr <= 'h' and
        1 <= coord2_int <= 8 and 'a' <= coord2_ltr <= 'h' and
        (-1 <= coord1_int - coord2_int <= 1) and 
        (-1 <= ord(coord1_ltr) - ord(coord2_ltr) <= 1)):
    print('да')
else:
    print('нет')

# Ввод 1:
# a1
# a1
# нет

# Ввод 2:
# f8
# f9
# нет

# Ввод 3:
# b2
# c3
# да
