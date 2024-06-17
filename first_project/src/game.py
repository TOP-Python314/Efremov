"""
Исполнительный модуль — игровой процесс.
"""

# текущий проект
import data, files, utils, players


def set_mode() -> None:
    """Управляет ветвлением запросов к игроку при настройке игрового процесса в начале новой партии."""
    mode = utils.test_command(data.MESSAGES['ввод режима'],
                              data.MESSAGES['некорректный выбор'],
                              ['1', '2'])
    if mode == '1':
        bot = utils.test_command(data.MESSAGES['ввод уровня'],
                                 data.MESSAGES['некорректный выбор'],
                                 ['1', '2'])
        data.bot = ['easy bot' if bot == '1' else 'hard bot'][0]
        data.active_players_names.append(data.bot)
        # Добавление функции хода бота
    else:
        name2 = players.get_player_name()
        # Добавление функции хода игрока
    print('set mode выполнен')
    
def load() -> bool:
    """Управляет загрузкой партии. Выводит два последних хода сохранённой партии."""
    saves = files.read_saves()
    players = str(frozenset(data.active_players_names))
    if players in saves:
        agree_load_game = utils.test_command(data.MESSAGES['загрузка сохранения'],
                                             data.MESSAGES['подтверждение или отказ'],
                                             data.COMMANDS['согласие'],
                                             data.COMMANDS['отказ']) 
        if agree_load_game in data.COMMANDS['согласие']:
            game_set = saves[players] # [token: name, dim, moves]
            data.player_token = game_set[0]
            data.dim = game_set[1]
            data.moves = game_set[2]
            return True
    print('load Выполнен')
    return False
    

def new_game_parameters() -> None:
    """ Управляет параметрами новой игры """
    token = utils.test_command(data.MESSAGES['ввод токена'],
                               data.MESSAGES['некорректный выбор'],
                               ['1', '2'])
    
    data.player_token = {'X': data.active_players_names[1 - int(token)]}
    data.dim = int(utils.test_command(data.MESSAGES['ввод размерности'],
                                      data.MESSAGES['некорректная размерность'],
                                      [str(i) for i in range(3, 21)]))
    data.field = utils.field_template(int(data.dim))
    data.wins = utils.wins(data.dim)
    return None
    
def game() -> data.GameStats:
    """Управляет игровым процессом партии."""
    print(' начата настройка игрового процесса')
    set_mode() # задает параметры партии
    game_load = load() # загружает параметры сохраненной партии если они есть
    print(game_load)
    if game_load == False:
        print('new game')
        new_game_parameters()
    else:
        print('load game')
    
    
    
def save() -> None:
    """Добавляет данные текущей партии в словарь сохранений и обновляет файлы данных."""
    saves = utils.all_saves()
    with open(saves_path, 'a', encoding='utf-8') as sp:
        # Преобразование ключа и сохранение словаря в файл
        game_set = {str(frozenset(data.active_players_names)): [data.player_token,
                                                                data.dim,
                                                                data.moves[-2:]]}
        saves.update(game_set)
        json.dump(saves, sp)


def print_board(alignment: data.Pointer) -> None:
    """Отправляет в stdout игровое поле с токенами сделанных ходов.
    
    :param alignment: индекс-указатель на текущий токен (0 - выравнивание влево, 1 - выравнивание вправо)
    """
    


def is_won(pointer: data.Pointer) -> bool:
    """Проверяет наличие победной комбинации для текущего игрока.
    
    :param pointer: индекс-указатель на текущий токен
    """
    ...