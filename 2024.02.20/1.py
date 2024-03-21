from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from operator import add, sub, neg, mul
from itertools import chain

RawRow = Iterable[Number]
RawMatrix = Iterable[RawRow]

class Matrix:
    """ Моделирует и изменяет матрицу """
    def __init__(self, raw_matrix: RawMatrix):
        """ Конструктор класса
        
        :param raw_matrix: строки матрицы
        """
        if self.is_valid(raw_matrix):
            self.__rows = raw_matrix
            self.n = len(raw_matrix) # количество рядов
            self.m = len(raw_matrix[0]) # количество столбцов
        
    
    @staticmethod 
    def is_valid(raw_matrix: RawMatrix) -> bool:
        """ Проверяет, является ли переданный аргумент подходящим объектом для конструирования матрицы """
        try:
            test_raw_matrix = iter(raw_matrix)
            for row in raw_matrix:
                test_raw_matrix = iter(row)
        except TypeError:
            print('TypeError: Матрица и ее ряды должныбыть итерируемыми объектами')
            return False
        
        for row in raw_matrix:
            if len(row) != len(raw_matrix[0]):
                print('ValueError: Все ряды матрицы должны быть одинаковой длины ')
                return False
        try:
            for row in raw_matrix:
                sum(row)
        except TypeError:
            print('TypeError: Все элементы матрицы должны быть вещественными числами')
            return False
            
        return True
    
    @property
    def transpose(self) -> Self:
        """ Возвращает транспонированную матрицу """
        
        return self.__class__([[self.__rows[column][row] for column in range(self.n)] for row in range(self.m)])
        
        
    def __getitem__(self: Self, index: int) -> list[Number]:
        """ Обеспечивает доступ на чтение к строкам матрицы по индексу """
        return self.__rows[index]
        
    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        if isinstance(other, Number):
            return self.__class__([[operation(self[i][j], other) for j in range(self.m)] for i in range(self.n)])
        elif isinstance(other, self.__class__):
            if operation is mul and self.n == other.m:
                return self.__class__([[sum([operation(self[k][i], other[i][j]) for i in range(self.m)]) for j in range(self.n)] for k in range(len(other))])
            if self.n == other.n and self.m == other.m:
                return self.__class__([[operation(self[i][j],  other[i][j]) for j in range(self.m)] for i in range(self.n)])
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')

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
        return self.__element_wise_operation(mul, other)

    def __rmul__(self, other) -> Self:
        return self.__element_wise_operation(mul, other)

    def __neg__(self) -> Self:
        return self.__element_wise_operation(mul, -1)

    def __repr__(self):
        return '\n'.join([' '.join([str(j) for j in i]) for i in self.__rows])
        
# >>> m1 = Matrix([[1, 2, 3], [4, 5, 6]])       
# >>> m2 = Matrix([[3, 3, 3], [3, 3, 3]]) 
# >>>
# >>> m1
# 1 2 3
# 4 5 6
# >>>
# >>> m2
# 3 3 3
# 3 3 3
# >>>
# >>> for i in range(m1.n):
# ...     for j in range(m1.m):
# ...             print(m1[i][j], end=' ')
# ...
# 1 2 3 4 5 6 >>>
# >>>
# >>> m2.transpose
# 3 3
# 3 3
# 3 3
# >>>
# >>> m1 + m2
# 4 5 6
# 7 8 9
# >>>
# >>> m1 - m2
# -2 -1 0
# 1 2 3
# >>>
# >>> m1 * m2
# 3 6 9
# 12 15 18
# >>>
# >>> 5 + m1
# 6 7 8
# 9 10 11
# >>>
# >>> 10 - m1
# 9 8 7
# 6 5 4
# >>>
# >>> m1[0][2] = 7
# >>> m1[1][2] = 8
# >>> m1
# 1 2 7
# 4 5 8
# >>>
# >>> m1.transpose
# 1 4
# 2 5
# 7 8
# >>>
# >>> m3 = Matrix([[1, 2], [3, 4]])
# >>> m3 + m1
# ValueError: сложение и вычитание возможно только для матриц одной размерности
# >>>
# >>> m3 * 3.9
# 3.9 7.8
# 11.7 15.6
# >>>
# >>> -m3
# -1 -2
# -3 -4
# >>>