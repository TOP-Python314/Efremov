def numbers_strip(numbers: list, n: int = 1, *, copy: bool = False) -> list:

    if copy == True:
        return numbers.copy()
    else:
        for i in range(n):
            numbers.remove(max(numbers))
            numbers.remove(min(numbers))
        return numbers
 
# >>> sample = [324, 12, 654, 23, 9, 76, 35]
# >>> sample_stripped = numbers_strip(sample)
# >>> sample_stripped
# [324, 12, 23, 76, 35]
# >>> sample is sample_stripped
# True

# >>> sample = [11, 33, 22, 44, 66, 55]
# >>> sample_stripped = numbers_strip(sample, 2, copy = True)
# >>> sample_stripped
# [11, 33, 22, 44, 66, 55]
# >>> sample is sample_stripped
# False
