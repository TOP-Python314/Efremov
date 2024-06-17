import draw, test, bot, json

""" Шаблон поля """
def field_template(cells):
    line = (cells-1) * ' {} |' + ' {} \n'
    a = line + (cells-1) * '————' + '———\n'   
    return a * (cells-1) + line

""" Запускает игровой процес """
# def game(player1: str, player2: str, lvl_bot: 'function', all_cells:int = 9):
def game(game_set: dict, mode: 'function'):
    # {frozenset(('name1', 'name2')): {'x': 'player1', 'moves': [1, 2, 3], 'dim': 3}}   
    names = list(game_set.keys())[0] # frozenset({'name1', 'name2'}) 
    xo = [game_set[names]['x']]
    [xo.append(name) if name not in xo else None for name in names]
    
    players_stats = dict([finds_name(name) for name in names]) # {'name1': [победа, поражение, ничья], 'name2': [победа, поражение, ничья]}
    cells = int(game_set[names]['dim'])
    board = [' ']*cells**2
    
    info = f' Чтобы поставить токен в нужную ячейку, введите номер клетки. Нумерация клеток от 0 до {cells}\n\n{field_template(cells)}\n'
    # добавить проверку на допустиммый ввод   
    list(list(game_set.values())[0].values())[0]
    
    moves_made = []   
    turn = 0
    flag = None
    while flag == None:
        print(field_template(cells).format(*board))
        if turn == 0:
            step = test.step_test(moves_made)
            board[step] = 'X'
            turn = 1
        else:
            step = mode(moves_made)
            board[step] = 'O'
            turn = 0
            
        moves_made.append(step)
        flag = test.win_test(cells, moves_made)
    
    print(field_template(cells).format(*board))
    if flag == 'xo':
        players_stats[xo[0]][2] += 1
        players_stats[xo[1]][2] += 1
        print(f' Поздравляю игроков с Ничьей! ')
    else:
        players_stats[xo[0-flag]][0] += 1
        players_stats[xo[1-flag]][1] += 1
        print(f' Поздравляю игрока {xo[flag]} с победой! ')

    
    finds_name(xo[0], players_stats[xo[0]]) # перезапись статистики игрока1
    finds_name(xo[1], players_stats[xo[1]]) # перезапись статистики игрока2

""" Обновляет статистику игроков игроков | Добавляет новый игроков """
def finds_name(name: str, stats:list = [0, 0, 0]) -> dict:
    with open('data_players.txt', 'r', encoding='utf-8') as dp:
        data_load = json.loads(dp.read())
        data_load[name] = stats
    with open('data_players.txt', 'w', encoding='utf-8') as dp:
        dp.write(json.dumps(data_load))
    return (name, data_load[name])

""" Задает параметры новой игры """
def new_game(name1, name2):
    select_turn = input(f' {name1}, вы хотите играть за "Х" или за "О" ?: ').lower()
    board_size = input(f' Выберите размер игрового поля от 3 до 24: ')
    return {frozenset((name1, name2)): {'x': [name1 if select_turn in ('x', 'х') else name2][0], 
                                        'moves': [], 
                                        'dim': board_size}}
    
""" Находит и загружает сохраненную игру """
def find_save_game(name1, name2) -> dict:
    with open('save_games.txt', 'r', encoding='utf-8') as sg:
        saves_load = json.loads(sg.read())
        game_set = frozenset((name1, name2))
        if game_set in saves_load:
            play = input(f' Хотите загрузить сохраненную игру? да/нет -> ')
            if play == 'да':
                return {frozenset((name1, name2)): saves_load[game_set]}
            else:
                return new_game(name1, name2)
        else:
            return new_game(name1, name2)
                
""" Запуск режима одиночной игры """
def solo_play(player):
    players_data = find_save_game(player, 'bot')
    lvl_bot = input(' Выберите уровень сложности -> easy/normal/hard: ')
    if lvl_bot == 'easy':
        game(players_data, bot.easy_bot)
    elif lvl_bot == 'normal':
        game(players_data, bot.normal_bot)
    elif lvl_bot == 'hard':
        game(players_data, bot.hard_bot)
    
""" Запуск режима кооперативной игры """    
def coop_play(player1):
    player2 = input(' Введите имя второго игрока: ')
    players_data = find_save_game(player1, player2)
    game(players_data, test.step_test)
    
""" Запускает игру """    
def start_play(player):
    print(f' Погнали, {player}!\n')
    players_select = input(' Хотите играть один или с другом? solo/coop: ')
    if players_select == 'solo':
        solo_play(player)
    else:
        coop_play(player)