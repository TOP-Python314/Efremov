def math_function_resolver(func, *rng: tuple[float], res_to_str = False) -> list:
    if res_to_str:
        return [str(round(func(i))) for i in rng]
    else:
        return [round(func(i)) for i in rng]
    
# >>> math_function_resolver(lambda x: x**3/15, *range(-5, 6))
# [-8, -4, -2, -1, 0, 0, 0, 1, 2, 4, 8]

# >>> math_function_resolver(lambda x: (x - 5.4)*12, *range(-2, 10, 2), res_to_str = True)
# ['-89', '-65', '-41', '-17', '7', '31']