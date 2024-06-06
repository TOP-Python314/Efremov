from numbers import Number
from collections.abc import Iterable
from typing import Self, Callable
from functools import cache, cached_property
from operator import add, sub, neg, mul
from itertools import repeat

class Matrix:
    """Класс моделирует неизменяемую матрицу"""
    
    def __init__(self, *args: Number, n: int, m: int):
        """Конструктор экземпляра класса.
        
        :param *args: элементы матрицы
        :param n: количество строк
        :param m: количество столбцов
        """
        if self.is_valid(*args, row=n, col=m):
            self.__flat: tuple[Number, ...] = args
            self.n = n
            self.m = m
            self.__transpose: Iterable[Number] = []
            for i in range(m):
                self.__transpose += list(args[i::m])
    
    
    @staticmethod
    def is_valid(*args: Number, row: int, col: int) -> bool:
        """Метод проверяет, является ли аргумент подходящим объектом для конструирования матрицы"""
        if len(args) != row * col:
            raise ValueError('невозможно сконструировать матрицу: некорректные размеры')
        for num in args:
            if not isinstance(num, Number):
                raise ValueError('невозможно сконструировать матрицу: элементами матрицы должны быть числа')
        return True

    # ИСПРАВИТЬ: здесь будет уместен cached_property
    @cached_property
    def transpose(self: Self) -> Self: 
        """Метод возвращает транспонированную матрицу"""
        return self.__class__(*self.__transpose, n=self.m, m=self.n)

    def __element_wise_operation(self, operation: Callable, other: Self | Number) -> Self:
        """Выполняет переданную операцию со своим и переданным объектом"""
        if isinstance(other, Number):
            return self.__class__(*(operation(num, other) for num in self.__flat), n=self.n, m=self.m)
        elif isinstance(other, self.__class__):
            if self.n == other.n and self.m == other.m:
                # КОММЕНТАРИЙ: как раз в этой реализации можно было попроще реализовать операции (см. пример)
                return self.__class__(*(operation(self.__flat[i], other.__flat[i]) for i in range(len(self.__flat))), n=self.n, m=self.m)
            else:
                raise ValueError('сложение и вычитание возможно только для матриц одной размерности')
        else:
            raise ValueError('алгебраические операции возможны только с матрицами и числами')

    def __add__(self, other) -> Self:
        return self.__element_wise_operation(add, other)

    def __radd__(self, other) -> Self:
        return self.__add__(other)

    def __sub__(self, other) -> Self:
        return self.__element_wise_operation(sub, other)

    def __rsub__(self, other) -> Self:
        return -self.__sub__(other)

    def __mul__(self, other) -> Self:
        if isinstance(other, Number):
            return self.__class__(*(num * other for num in self.__flat), n=self.n, m=self.m)
        elif isinstance(other, self.__class__):
            raise NotImplementedError('умножение матриц будет реализованно в будущем')

    def __rmul__(self, other) -> Self:
        return self.__mul__(other)

    def __neg__(self) -> Self:
        return self.__mul__(-1)

    def __repr__(self):
        # КОММЕНТАРИЙ: ух!... (см. пример)
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