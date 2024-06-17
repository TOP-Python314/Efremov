import json, configparser as cp

config = cp.ConfigParser()

player_name = 'name1'
player_stats = {'win': 1, 'lose': 3, 'draw': 2}
config.add_section(player_name)
config[player_name] = player_stats

with open('test.ini', 'w', encoding='utf-8') as t:
    config.write(t)
    
config.read('test.ini')
int(config['name1']['win'])

config.has_section('name4') # False

config.has_section('name1') # True
