set1 = input()
set2 = ['1', '0', 'b']

if set(set1) - set(set2) != set():
    print('нет')
else:
    if (set1[0] == 'b' or
            set1[:2] == '0b' or
            set(set1) - {'1', '0'} == set()):
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