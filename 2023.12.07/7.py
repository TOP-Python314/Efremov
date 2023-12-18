list_of_dicts = [
    {
        'Барнаул': 7,
        'Владивосток': 9,
        'Волгоград': 9,
        'Ижевск': 5,
        'Махачкала': 7,
        'Москва': 9,
        'Омск': 9,
        'Саратов': 4,
        'Ульяновск': 3
    },
    {
        'Казань': 8,
        'Краснодар': 2,
        'Москва': 3,
        'Самара': 3,
        'Санкт-Петербург': 6,
        'Тюмень': 1,
        'Уфа': 7
    },
    {
        'Ижевск': 1,
        'Иркутск': 3,
        'Кемерово': 1,
        'Москва': 3,
        'Саратов': 3,
        'Хабаровск': 6
    },
    {
        'Барнаул': 7,
        'Оренбург': 3,
        'Санкт-Петербург': 1,
        'Тюмень': 4,
        'Ярославль': 3
    }
]

new_list_of_dicts = {}
for citys in list_of_dicts:
    for city in citys:
        if city not in new_list_of_dicts:
            new_list_of_dicts[city] = [citys[city]]
        else:
            new_list_of_dicts[city].append(citys[city])
 

for key, vallue in new_list_of_dicts.items():
    print(f'{key}: {set(vallue)}')
    
# Вывод: 
    # Барнаул: {7}
    # Владивосток: {9}
    # Волгоград: {9}
    # Ижевск: {1, 5}
    # Махачкала: {7}
    # Москва: {9, 3}
    # Омск: {9}
    # Саратов: {3, 4}
    # Ульяновск: {3}
    # Казань: {8}
    # Краснодар: {2}
    # Самара: {3}
    # Санкт-Петербург: {1, 6}
    # Тюмень: {1, 4}
    # Уфа: {7}
    # Иркутск: {3}
    # Кемерово: {1}
    # Хабаровск: {6}
    # Оренбург: {3}
    # Ярославль: {3}