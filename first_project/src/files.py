import data, configparser, json

def read_players() -> data.Players:    
    """Читает из файла данные об игроках и их статистике и возвращает словарь игроков с требуемой структурой данных."""
    config = configparser.ConfigParser()
    config.read('players.ini')
    players_data = {}
    for i in config.sections():
        players_data[i] = dict(config[i].items())
    return players_data      


def read_saves() -> data.Saves:
    """Читает из файла данные о сохранённых партиях и возвращает словарь сохранений с требуемой структурой данных."""
    names = data.active_players_names
    with open(data.saves_path, 'r', encoding='utf-8') as sp:
        saves_txt = sp.read()
        saves = [{} if saves_txt == '' else json.loads(saves_txt)][0]
        return saves

def write_players(players_data: data.Players) -> None:
    """Записывает в файл данные об игроках и их статистике."""
    name_player = list(players_data.keys())[0]
    win, lose, draw = list(players_data.values())[0]   
    config.add_section(name_player)
    config[name_player] = {'win': win, 'lose': lose, 'drow': drow}
    with open(data.players_path, 'w', encoding='utf-8') as player:
        config.write(player)

def write_saves(saves_data: data.Saves) -> None:
    """Записывает в файл данные о сохранённых партиях."""
    
    ...