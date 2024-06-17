import json
""" Создает список выйгрышных комбинаций """
def wins(cells: int) -> list:
    wins = []
    for i in range(cells):
        wins.append({*range(i*cells, (i+1)*cells)})
        wins.append({*range(i, cells**2, cells)})
    wins.append({*range(0, cells**2, cells+1)})
    wins.append({*range(cells-1, cells**2-1, cells-1)})
    return wins

""" Проверяет наличие выйгрышной комбинации """
def win_test(cells, moves: list) -> str | list:
    moves1 = [moves[i] for i in range(0, len(moves), 2)] # ходы для крестика   
    moves2 = [moves[i] for i in range(1, len(moves), 2)] # ходы для нолика
    vars_moves1 = list(filter(lambda x: len(x & set(moves2)) == 0, wins(cells))) # список оставшихся возможных комбинаций для крестика
    vars_moves2 = list(filter(lambda x: len(x & set(moves1)) == 0, wins(cells))) # для нолика
    if len(vars_moves1) == 0 and len(vars_moves2) == 0:
        game_end = input(f' Возможные комбинации побед закончились. Партия будет закончена в ничью. Хотите продолжить игру? да/нет ')
        if game_end == 'да':
            return 'xo'
    elif any(set(moves1)>=win for win in vars_moves1):
        return 0
        # победа крестика
    elif any(set(moves2)>=win for win in vars_moves2):
        return 1
        # победа нолика

""" Проверяет занята ячейка или нет """
def step_test(moves: list) -> int:
    step = int(input(' Введите номер клетки: '))
    while True:
        if step in moves:
            step = int(input(' Данная клетка уже занята\n'))
        else:
            return step
            

names1 = ('name1', 'name2')
names2 = ('name3', 'name4')
names3 = ('name1', 'name3')

token1 = {'name1': 'X'}
token2 = {'name3': 'O'}

moves1 = [1, 2, 3, 4]
moves2 = [4, 8, 12]

dim1 = 3
dim2 = 5

def load():
    with open('data/saves.ttt', 'r', encoding='utf-8') as sp:
        a = sp.read()
        print(type(a))
        if a == '':
            b = {}
        else:
            b = json.loads(a)
        return b
        
def save(names: tuple, token: dict, moves: list, dim: int) -> None:
    """Добавляет данные текущей партии в словарь сохранений и обновляет файлы данных."""
    load_game = load()
    with open('data/saves.ttt', 'w', encoding='utf-8') as sp:
        # Список активных игроков
        #data.active_players_names
        # размер поля
        #data.dim
        # кто играет за "Х"
        #name = dict[str, str]
        # Последние 2 сделанных хода
        #move_made = list[int, int]
        # Преобразование ключа и сохранение словаря в файл
        
        print(load_game)
        game_set = {str(frozenset(names)): [token, dim, moves]}
        load_game.update(game_set)
        print(load_game)
        json.dump(game_set, sp)   
b = {'a': '1', 'b': '2', 'c': '3'} 
def a(comand ,*args):
    flag = True
    
    print(args)
    print(comand)
    
    while flag == True:
            if comand in args:
                    return comand
                    flag = False
            else:
                    comand = input('Не корректный ввод. Повторите -> ')
