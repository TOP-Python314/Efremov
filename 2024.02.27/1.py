class Point: 
    """Класс описывает точку с координатами x, y"""
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
        
    @property
    def x(self) -> float:
        """Возвращает x"""
        return self.__x
        
    @x.setter
    def x(self, new_x) -> None:
        """Возвращает исключение при изменении x"""
        raise TypeError(f'{self.__class__.__name__} object does not support coordinate assignment')
        
    @property    
    def y(self) -> float:
        """Возвращает y"""
        return self.__y
        
    @y.setter
    def y(self, new_y) -> None:
        """Возвращает исключение при изменении y"""
        raise TypeError(f'{self.__class__.__name__} object does not support coordinate assignment')

    def __repr__(self):
        return f'{(self.x, self.y)}'
        
    def __str__(self):
        return repr(self)
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.x == other.x and self.y == other.y    
        
class Line:   
    """Класс описывает отрезок с координатами (x, y) для начальной и конечной точек"""
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end
        
    @staticmethod   
    def __length_calc(point1: Point, point2: Point) -> float:
        """Возвращает длину отрезка"""
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5
        
    @property
    def start(self) -> Point:
        """Возвращает start"""
        return (self.__start.x, self.__start.y)
        
    @start.setter
    def start(self, new_start: Point) -> None:
        """Устанавливает новое значение start"""
        if not isinstance(new_start, Point):
            raise TypeError(
                f"'start' attribute of '{self.__class__.__name__}'"
                f"object supports only '{self.__start.__class__.__name__}'"
                f"object assignment"
            )
        self.__start = new_start
        
    @property
    def end(self) -> Point:
        """Возвращает end"""
        return (self.__end.x, self.__end.y)
        
    @end.setter
    def end(self, new_end: Point):
        """Устанавливает новое значение end"""
        if not isinstance(new_end, Point):
            raise TypeError(
                f"'start' attribute of '{self.__class__.__name__}'"
                f"object supports only '{self.__start.__class__.__name__}'"
                f"object assignment"
            )
        self.__end = new_end
        
    @property
    def length(self) -> float:
        """Вычисляет и возвращает значение length"""
        return self.__length_calc(self.start, self.end)
        
    @length.setter
    def length(self, new_length) -> None:
        """Возвращает исключение при изменении length"""
        raise TypeError(f'{self.__class__.__name__} object does not support length assignment')
    
    def __repr__(self):
        return(f'{self.start}---{self.end}')
        
    def __str__(self):
        return repr(self)
        
       
class Polygon(list): 
    """Класс описывает многоугольник на координатной плоскости"""
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: tuple[Line, ...]):
        super().__init__((side1, side2, side3, *sides))
    
    def is_closed(self) -> bool:
        """Проверяет замкнут многоуголник или нет"""
        for i in range(len(self)):
            if self[i].start != self[i-1].end:
                return False
        else:
            return True
            
    @property 
    def perimeter(self) -> float:
        """Вычисляет и возвращает периметр многоугольника"""
        if self.is_closed():
            return sum(line.length for line in self)
        else:
            raise ValueError("line items doesn't from a closed plygon")
            
    @perimeter.setter
    def perimeter(self, new_perimeter):
        """Возвращает исключение при изменении perimeter"""
        raise AttributeError(f"property 'perimeter' of '{self.__class__.__name__}' object has no setter")

# >>> p1 = Point(1, 3)
# >>> p2 = Point(9, 1)
# >>> p3 = Point(8, 7)
# >>> p4 = Point(3, 10)
# >>>
# >>> p1
# (1, 3)
# >>> repr(p2) == str(p2)
# True
# >>> p3 == Point(8, 7)
# True
# >>> p4 == Point(18, 45)
# False
# >>> p2.x, p2.y
# (9, 1)
# >>> p3.y = 4
# TypeError: Point object does not support coordinate assignment
# >>>
# >>> l1 = Line(p1, p2)
# >>> l2 = Line(p2, p3)
# >>> l3 = Line(p3, p4)
# >>> l4 = Line(p4, p1)
# >>>
# >>> l1
# (1, 3)---(9, 1)
# >>>
# >>> repr(l3) == str(l3)
# True
# >>>
# >>> l2.length
# 6.082762530298219
# >>>
# >>> l4.length = 12
# TypeError: Line object does not support length assignment
# >>>
# >>> l1.start = 3
# TypeError: 'start' attribute of 'Line'object supports only 'Point'object assignment
# >>>
# >>> pol1 = Polygon(l1, l2, l3, l4)
# >>>
# >>> pol1.perimeter
# 27.440035565659358
# >>> pol1.perimeter = 44
# AttributeError: property 'perimeter' of 'Polygon' object has no setter
# >>>
# >>> l3.end = Point(-32, -32)
# >>> pol1.perimeter
# ValueError: line items doesn't from a closed plygon
# >>>    