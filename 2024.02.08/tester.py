class ChessKing:
    """Шахматная фигура короля.
    
    :attr fiels: соответствие между буквой, обозначающей вертикаль шахматной доски и числом:
    :attr ranks: соответствие между строковым представлением числа (горизонталь) и числом:
    """
    fiels: dict[str, int] = {'abcdefgh'[i]: i+1 for i in range(8)}
    ranks: dict[str, int] = {'12345678'[i]: i+1 for i in range(8)} 
    
    
    def __init__(self, color: str = 'white', square: str = None):
        """
        :attr color: цвет фигуры
        :attr square: поле шахматной доски, где в данный момент находится фигура
        """
        self.color = color
        self.square = {'white': 'e1', 'black': 'e8'}[color] if not square else square
        
        
    def is_turn_valid(self, new_square: str) -> bool:
        """Метод проверяет возможен ли для данной фигуры ход в новое поле.
        
        :param new_square: новое поле, в которую осуществляется ход
        :return: объект логического типа - результат проверки
        """
        fiels = self.__class__.fiels
        ranks = self.__class__.ranks
        
        new_fiel = new_square[0]
        new_rank = new_square[1]
        
        if new_fiel not in fiels or new_rank not in ranks or self.square == new_square:
            return False
        files_start, ranks_start = ord(self.square[0]), int(self.square[1])
        files_end, ranks_end = ord(new_fiel), int(new_rank)
        return abs(files_start - files_end) <= 1 and abs(ranks_start - ranks_end) <= 1
        
    
    def turn(self, new_square: str) -> None:
        """Метод выполняет ход фигурой.
        
        :param new_square: новое поле, в которую осуществляется ход
        """
        if self.is_turn_valid(new_square):
            self.square = new_square
        else:
            raise ValueError("Несоответствующее значение")

    
    def __str__(self):
        for key, value in globals().items():
            if self is value:
                name = key
                return f'{name.upper()}: {self.square}'
            
        
    def __repr__(self):
        for key, value in globals().items():
            if self is value:
                name = key
                return f'{name.upper()}: {self.square}'