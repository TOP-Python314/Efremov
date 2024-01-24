from datetime import datetime as dt

def logger(func: 'function') -> 'function':
    """ Создает вводимую функцию с именем и параметрами в виде строки 
        Проверяет на ошибки
        Сохраняет в лог"""
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
        time_format = dt.now().strftime("%Y.%M.%d %H:%m:%S")
        fc = open('data/function_calls.log', 'a', encoding='utf-8')
        try:
            test_func = func(*args, **kwargs)
        except Exception as exc:
            text_out = f'{time_format} - {func_body} .. {type(exc).__name__}: {exc}\n'
            print(text_out)
            fc.write(text_out)
            fc.close()
        else:
            print(f'{time_format} - {func_body} -> {func(*args, **kwargs)}\n{func(*args, **kwargs)}')
            fc.write(f'{time_format} - {func_body} -> {func(*args, **kwargs)}\n')
            fc.close()
    return wrapper  
    
# D:\TOP\Python\Выполнено\Efremov\2023.12.28>python -i 5.py
# >>> def func_procent(num1, num2):
# ...     return round(num1/num2*100)
# ...
# >>> func_procent = logger(func_procent)
# >>> func_procent(70, 145)
# 2024.20.24 11:01:14 - func_procent(70, 145) -> 48
# 48
# >>> ^Z


# D:\TOP\Python\Выполнено\Efremov\2023.12.28>type data\function_calls.log
# 2024.20.24 11:01:14 - func_procent(70, 145) -> 48

# D:\TOP\Python\Выполнено\Efremov\2023.12.28>python -i 5.py
# >>>
# >>> def test_func():
# ...     pass
# ...
# >>> test_func = logger(test_func)
# >>> test_func()
# 2024.22.24 11:01:01 - test_func() -> None
# None
# >>> ^Z


# D:\TOP\Python\Выполнено\Efremov\2023.12.28>type data\function_calls.log
# 2024.20.24 11:01:14 - func_procent(70, 145) -> 48
# 2024.22.24 11:01:01 - test_func() -> None