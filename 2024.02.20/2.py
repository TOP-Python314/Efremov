from functools import cached_property, cache
from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from operator import add, sub, neg, mul
from itertools import repeat

RawRow = Iterable[Number]
RawMatrix = Iterable[RawRow]

class Matrix:

    def __init__(self, *args: Number, n: int, m: int):
        if self.is_valid(*args, row=n, col=m):
            self.__flat: tuple[Number, ...] = args
            self.n = n
            self.m = m
            self.__transpose: Iterable[Number] = []
            for i in range(m):
                self.__transpose += list(args[i::m])
        
        
    @staticmethod 
    def is_valid(*args: Number, row: int, col: int) -> bool:
        """ Проверяет, является ли переданный аргумент подходящим объектом для конструирования матрицы """
        try:
            sum(args)
        except TypeError:
            raise TypeError('Все элементы матрицы должны быть вещественными числами')
        try:
            test_raw_matrix = iter(args)
        except TypeError:
            raise TypeError('Матрица и ее ряды должныбыть итерируемыми объектами')
        if len(args)%col != 0:
            raise ValueError('невозможно сконструировать матрицу: некорректные размеры')
        return True

    @cached_property
    def transpose(self: Self) -> Self:
        """ Возвращает транспонированную матрицу """
        
        return self.__class__(*self.__transpose, n=self.m, m=self.n)
        
    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        if isinstance(other, Number):
            print('other Number')
            return self.__class__(*(operation(num, other) for num in self.__flat), n=self.n, m=self.m)
        elif isinstance(other, self.__class__):
            
            if self.n == other.n and self.m == other.m:
                print('operation sum')
                return self.__class__(*(operation(self.__flat[i], other.__flat[i]) for i in range(len(self.__flat))), n=self.n, m=self.m)
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')
        else:
            raise ValueError('алгебраические операции возможны только с матрицами и числами')        
    def __add__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __radd__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(sub, other)

    def __rsub__(self, other) -> Self:
        sub_matrix = -self
        return sub_matrix.__element_wise_operation(add, other)

    def __mul__(self, other) -> Self:
        if isinstance(other, Number):
            return self.__class__(*(num * other for num in self.__flat), n=self.n, m=self.m)
        elif isinstance(other, self.__class__):
            raise NotImplementedError('умножение матриц будет реализованно в будущем')

    def __rmul__(self, other) -> Self:
        return self.__element_wise_operation(mul, other)

    def __neg__(self) -> Self:
        return self.__element_wise_operation(mul, -1)
    
    def __repr__(self):
        
        if abs(min(self.__flat)) > abs(max(self.__flat)):
            num_format = f'>{str(len(str(min(num for num in self.__flat))))}'
        else:
            num_format = f'>{str(len(str(max(num for num in self.__flat))))}'
        
        rep_lines = []
        for i in range(0, len(self.__flat), self.m):
            rep_lines.append(
                " ".join(f"{round(num, 1):{num_format}}" 
                for num in self.__flat[i:i + self.m])
            )
        representation = '\n'.join(f'{rep}' for rep in rep_lines)
        return representation 
        
# >>> Matrix(1, 2, 3, 4, 5, n=2, m=3)
# ValueError: невозможно сконструировать матрицу: некорректные размеры
# >>> m1 = Matrix(*repeat(1, 15), n=3, m=5)
# >>> m2 = Matrix(*range(1, 16), n=3, m=5)
# >>>
# >>> m1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# >>>
# >>> m2
 # 1  2  3  4  5
 # 6  7  8  9 10
# 11 12 13 14 15
# >>>
# >>> m1[0][0]
# TypeError: 'Matrix' object is not subscriptable
# >>>
# >>> m2.transpose
 # 1  6 11
 # 2  7 12
 # 3  8 13
 # 4  9 14
 # 5 10 15
# >>>
# >>> m1 + m1
# operation sum
# 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2 2
# >>>
# >>> m2 - m1
# operation sum
 # 0  1  2  3  4
 # 5  6  7  8  9
# 10 11 12 13 14
# >>>
# >>> m1 * m2
# NotImplementedError: умножение матриц будет реализованно в будущем
# >>>
# >>> 3 + m1
# other Number
# 4 4 4 4 4
# 4 4 4 4 4
# 4 4 4 4 4
# >>>
# >>> m2.transpose - 10
# other Number
# -9 -4  1
# -8 -3  2
# -7 -2  3
# -6 -1  4
# -5  0  5
# >>>
# >>> -1.5 - m1
# other Number
# other Number
# -2.5 -2.5 -2.5 -2.5 -2.5
# -2.5 -2.5 -2.5 -2.5 -2.5
# -2.5 -2.5 -2.5 -2.5 -2.5
# >>>
# >>> m3 = Matrix(*range(1, 5), n=2, m=2)
# >>>
# >>> m3 + m1
# ValueError: сложение и вычитание возможно только для матриц одной размерности
# >>>
# >>> m3 * 4.5
 # 4.5  9.0
# 13.5 18.0
# >>>
# >>> -m3
# other Number
# -1 -2
# -3 -4
# >>> m3 - [4, 3, 2, 1]
# ValueError: алгебраические операции возможны только с матрицами и числами