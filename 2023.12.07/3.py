nums_1 = input()
nums_2 = input()

# if len(nums_1.split(nums_2)) > 1:
    # print('да')
# else:
    # print('нет')
    
a = [int(n) for n in nums_1.split()]
b = [int(n) for n in nums_2.split()]
flag = False
for i in range(len(nums_1) - len(nums_2)):
    if nums_2 == nums_1[i:len(nums_2)+i]:
        flag = True
        break
if flag:
    print('да')
else:
    print('нет')

# Ввод 1: 
    # 3 4 12 36 2 526
    # 4 12 36
    
    # да

# Ввод 2: 
    # 43 2 12 44 6 9
    # 43 12 9
    
    # нет