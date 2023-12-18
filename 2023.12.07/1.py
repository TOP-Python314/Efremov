mail = input()

if 0 < mail.find('@') < mail.rfind('.'):
    print('да')
else:
    print('нет')
    
# Ввод 1:
# evgenii.9802@gfail.com
# да

# Ввод 2:
# jony.mail@kz
# нет