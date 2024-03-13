class ChessKing:
    fiels: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8} # Вертикаль
    ranks: dict[str, int] = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8} # Горизонталь
    
    
    def __init__(self, color: str = 'white', square: str = None):
        """
        :attr color: цвет фигуры
        :attr square: положение шахматной фигуры в моменте
        """
        self.color: str = color
        self.square: str = {'white': 'e1', 'black': 'e8'}[color] if not square else square
        
       
    
    def is_turn_valid(self, new_square: str) -> bool:
        """ Проверяет возможность хода 
        :param new_square: новое поле, в которую осуществляется ход
        :return: объект логического типа - результат проверки
        """
        fiels = self.__class__.fiels
        ranks = self.__class__.ranks
        
        new_fiels = new_square[0]
        new_rank = new_square[1]
        
        if (new_fiels not in fiels or 
           new_rank not in ranks or 
           new_square == self.square):
                return False

        start_coord_y, start_coord_x = fiels[self.square[0]], ranks[self.square[1]]
        end_coord_y, end_coord_x = fiels[new_fiels], ranks[new_rank]
        
        return abs(start_coord_x - end_coord_x) <= 1 >= abs(start_coord_y - end_coord_y) 
        
    def turn(self, new_square: str) -> None:
        """ Ход фигуры 
        :param new_square: новое поле, в которую осуществляется ход
        """
        if self.is_turn_valid(new_square):
            self.square = new_square
        else:
            raise ValueError("Несоответствующее значение")
            
    def __repr__(self):
        for key, value in globals().items():
            if self is value:
                name = key
                return f'{name.upper()}: {self.square}'
    
    def __str__(self):
        for key, value in globals().items():
            if self is value:
                name = key
                return f'{name.upper()}: {self.square}'

# >>> wk = ChessKing()
# >>> wk.color
# 'white'
# >>> wk.square
# 'e1'
# >>> wk.turn('f2')
# >>> wk
# WK: f2
# >>> wk.turn('a4')
# ValueError: Несоответствующее значение
# >>> bk = ChessKing('black')
# >>> print(bk)
# BK: e8