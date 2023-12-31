def deck():
    num = range(2, 15)
    suit = ['черви', 'бубны', 'пики', 'трефы']
    for i in suit:
        for j in num:
            yield (j, i)
            
# >>> list(deck())[3::13]
# [(5, 'черви'), (5, 'бубны'), (5, 'пики'), (5, 'трефы')]