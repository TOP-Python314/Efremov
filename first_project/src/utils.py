"""
Вспомогательный модуль — дополнительные функции.
"""

# текущий проект
# import bot
import data
import json

def change_dimension(new_dimension: int) -> None:
    """Переопределяет все глобальные переменные, связанные с размером игрового поля."""
    data.dim = new_dimension
    data.all_cells = new_dimension**2
    data.dim_range = range(new_dimension)
    data.all_cells_range = range(data.all_cells)
    data.empty = dict.fromkeys(data.all_cells_range, ' ')
    data.field = generate_field_template(new_dimension)
    data.wins = generate_win_combinations(new_dimension)
    # data.start_matrices = (
        # bot.calc_sm_cross(),
        # bot.calc_sm_zero()
    # )
    data.MESSAGES['ход не в диапазоне'].format(data.all_cells-1)


def get_new_dimension() -> int:
    """Получает от пользователя новый размер игрового поля."""
    ...


def generate_field_template(dimension: int) -> str:
    """Возвращает строковый шаблон игрового поля требуемого размера."""
    ...


def generate_win_combinations(dimension: int) -> data.WinCombinations:
    """Возвращает список победных комбинаций номеров клеток игрового поля требуемого размера."""
    ...


def clear(delete_save: bool = False) -> None:
    """Перезаписывает начальными значениями глобальные переменные, связанные с игровым процессом."""
    ...



def columnize(text: str, column_width: int) -> list[str]:
    """Разбивает переданную строку на отдельные слова и формирует из слов строки, длины которых не превышают заданное значение (текст-колонка). Возвращает список строк, к которым впоследствии может быть применено любое выравнивание.
    
    :param text: текст для обработки
    :param column_width: ширина колонки в символах
    """
    multiline, line_len, i = [[]], 0, 0
    for word in text.split():
        word_len = len(word)
        if line_len + word_len + len(multiline[i]) <= column_width:
            multiline[i] += [word]
            line_len += word_len
        else:
            multiline += [[word]]
            line_len = word_len
            i += 1
    return [' '.join(line) for line in multiline]


def concatenate_rows(
        multiline1: str,
        multiline2: str,
        *multilines: str,
        padding: int = 8
) -> str:
    """Объединяет произвольное количество строк текстов-колонок в одну строку с несколькими колонками и отступом между ними.

    :param padding: ширина отступа между колонками в пробелах
    """
    multilines = multiline1, multiline2, *multilines
    multilines = [m.split('\n') for m in multilines]
    padding = ' '*padding
    return '\n'.join(
        padding.join(row)
        for row in zip(*multilines)
    )
        
def test_command(msg: str, answer: str, *cmds: list) -> str:
    """ Проверяет и перезапрос корректной команды """
    flag = True
    cmd = input(msg)
    while flag == True:
        if cmd in cmds[0]:
            flag = False
            return cmd
        else:
            cmd = input(answer)
            

def field_template(dim):
    """ Шаблон поля """
    line = (dim-1) * ' {} |' + ' {} \n'
    a = line + (dim-1) * '————' + '———\n'   
    return a * (dim-1) + line    


def wins(dim: int) -> list:
    """ Создает список выйгрышных комбинаций """
    wins = []
    for i in range(dim):
        wins.append({*range(i*dim, (i+1)*dim)})
        wins.append({*range(i, dim**2, dim)})
    wins.append({*range(0, dim**2, dim+1)})
    wins.append({*range(dim-1, dim**2-1, dim-1)})
    return wins  