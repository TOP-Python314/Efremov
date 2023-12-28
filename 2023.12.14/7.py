ss_dict = dict((chr(87+i), i) for i in range(10, 36))
for i in range(10):
    ss_dict[str(i)] = i
    
def int_base(num: str, ns_in: int, ns_out: int):
        """ Переводит число из произвольной СС в произвольную СС """
    if len(num.split('.')) == 1:
        return num_sys_n(num_sys_10(num, ns_in), ns_out)
    else:
        num1, num2 = num.split('.')
        return f'{num_sys_n(num_sys_10(num1, ns_in), ns_out)}.{num_sys_n(num_sys_10(num2, ns_in, False), ns_out, False)}'

def num_sys_10(num: str, ns_in: int, int_dec = True) -> int:
    """ Переводит целую/десятичную часть числа в десятичную степень """
    n = [ss_dict[i] for i in num]
    if int_dec:
        return sum([n[i]*ns_in**(len(num)-1-i) for i in range(len(num))])
    else:
        return sum([n[i]*ns_in**(-1-i) for i in range(len(num))])
    
def num_sys_n(num: int, ns_out: int, int_dec = True) -> str:
    """ Переводит целую/десятичную часть числа из десятичной степени в n-ую """
    num_out = ''
    if int_dec:
        
        n = num
        while ns_out <= n:
            num_out += [i for i, j in ss_dict.items() if j == n%ns_out][0]
            n //= ns_out
        num_out += [i for i, j in ss_dict.items() if j == n%ns_out][0]
        return num_out
    else:
        print(num)
        ln = len(str(num)) - 2
        n = num
        for k in range(ln):
            num_out += [i for i, j in ss_dict.items() if j == int((n*ns_out)//1)][0]
            n = round((n*ns_out)%1, ln)
        return num_out

    
    