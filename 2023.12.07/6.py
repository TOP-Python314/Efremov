set_1 = input()
set_2 = ['1', '0', 'b']

if set(set_1) - set(set_2) != set():
    print('нет')
else:
    if (set_1[0] == 'b' or
            set_1[:2] == '0b' or
            set(set_1) - {'1', '0'} == set()):
        print('да')
    else:
        print('нет')

# Ввод 1:
    # 0b101204045
    
    # нет
    
# Ввод 2:
    # 10101010111
    
    # да
    
# Ввод 3:
    # 0b101011110
    
    # да