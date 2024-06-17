"""
Точка входа. Управляющий код верхнего уровня
"""

# текущий проект
import data
import files
import help
import players
import utils
import game

def config():
    """Чтение файлов, инициализация структур данных, авторизация."""
    data.players_db = files.read_players()
    data.saves_db = files.read_saves()
    
    if not data.players_db:
        help.print_full_help()
    
    utils.change_dimension(3)
    
    data.authorized = players.get_player_name()
    
def main_menu():
    """Главное меню: обработка команд."""    
    name = data.authorized
    print(f'{name}, приветствую тебя в игре крестики нолики')
    print(*data.INTERFACE, sep='\n')

    command = input(data.MESSAGES['ввод команды'])
    flag = True
    while flag == True:
        if command in data.COMMANDS['начать новую партию']:
            game.game()
            
        elif command in data.COMMANDS['отобразить раздел помощи']:
            for text1, text2 in data.COMMANDS.items():
                print(text1, text2)
                
        elif command in data.COMMANDS['создать или переключиться на игрока']:
            player = players.get_player_name()
            
        elif command in data.COMMANDS['выйти']:
            end()
            
        else:
            data.MESSAGES['некорректная команда']

def end():
    """Перед завершением работы."""
    ...



if __name__ == '__main__':
    config()
    main_menu()
    end()