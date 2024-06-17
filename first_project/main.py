""" Первый проект """

import func, draw

print(' Приветствую тебя в игре "Крестики и Нолики" ')
name = input(' Введите свое имя: ')
player_stats = func.finds_name(name) # Статистика игрока
# Добавить проверку на не оконченные игры
start = input(f' {name}, желаете начать игру? да/нет: ').lower()

if start == 'да':
    func.start_play(name)
else:
    print(f' До скорой встречи, {name}! ')
    
        
        
