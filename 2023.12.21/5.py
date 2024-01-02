def logger(func: 'function') -> 'function':
    """ Создает вводимую функцию с именем и параметрами в виде строки 
        Проверяет на ошибки """
    def wrapper(*args, **kwargs):

        args_str = ''
        if len(args) > 0:
            args_str = '{}'.format(args[0])
            for i in range(1, len(args)):
                args_str += ', '+str(args[i])
                
        a = list(kwargs.items())
        kwargs_str = ''
        if len(a) > 0:
            kwargs_str = '{}={}'.format(a[0][0], a[0][1])
            for i in range(1, len(a)):
                kwargs_str += ', {}={}'.format(a[i][0], a[i][1])
        
        if args_str == '' == kwargs_str:
            func_body = '{}()'.format(func.__name__)
        elif args_str != '' != kwargs_str:
            func_body = '{}({}, {})'.format(func.__name__, args_str, kwargs_str )
        elif args_str == '':    
            func_body = '{}({})'.format(func.__name__, kwargs_str)
        else:
            func_body = '{}({})'.format(func.__name__, args_str)
        
        try:
            test_func = func(*args, **kwargs)
        except Exception as exc:
            print(f'{func_body} .. {type(exc).__name__}: {exc}')
        else:
            print(f'{func_body} -> {func(*args, **kwargs)}\n'
                  f'{func(*args, **kwargs)}')
    return wrapper  
    
# >>> def seconds_sum(hour, /, minutes=30, *, seconds=0):
# ...     return seconds+minutes*60+hour*3600
# ...
# >>> seconds_sum = logger(seconds_sum)
# >>>
# >>>
# >>> seconds_sum(3, 25, seconds=44)
# seconds_sum(3, 25, seconds=44) -> 12344
# 12344
# >>> seconds_sum(0, seconds=23)
# seconds_sum(0, seconds=23) -> 1823
# 1823
# >>> seconds_sum('a', minutes=23, seconds=10)
# seconds_sum(a, minutes=23, seconds=10) .. TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>>