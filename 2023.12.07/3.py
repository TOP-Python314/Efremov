nums1 = input()
nums2 = input()

# if len(nums_1.split(nums_2)) > 1:
    # print('да')
# else:
    # print('нет')
    
a = [int(n) for n in nums1.split()]
b = [int(n) for n in nums2.split()]
flag = False
for i in range(len(nums1) - len(nums2)):
    if nums2 == nums1[i:len(nums2)+i]:
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