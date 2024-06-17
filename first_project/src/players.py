"""
Исполнительный модуль — взаимодействие с игроком.
"""

# текущий проект
import data, files


def get_player_name() -> str:
    """Запрашивает имя игрока до соответствия с шаблоном. Добавляет в словарь игроков имя и начальную статистику, если имя является новым."""
    name = input(data.MESSAGES['ввод имени'])
    # добавить проверку имени
    if name in files.read_players():
        data.players_db[name] = files.read_players[name]
    else:
        data.players_db[name] = {'win': 0, 'lose': 0, 'drow': 0}
    data.active_players_names.append(name)
    return name


def update_stats(result: data.GameStats) -> None:
    """Обновляет статистику активных игроков по результатам партии."""
    


def get_human_turn() -> data.SquareIndex | None:
    """Запрашивает пользовательский ввод для хода во время партии до получения корректного ввода."""
    turn = input(' Введите номер ячейки: ')
    flag = True
    while flag == True:
        if set([turn]) <= data.all_cells_range:
            return turn
            flag = False
        else:
            turn = input(' Не допустимое значение. Введите номер ячейки еще раз: ')