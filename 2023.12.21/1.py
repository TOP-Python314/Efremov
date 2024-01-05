nominals = {
    'E6': (
        100, 150, 220, 330, 470, 680
    ),
    'E12': (
        100, 120, 150, 180, 220, 270, 330, 390, 470, 560, 680, 820
    ),
    'E24': (
        100, 110, 120, 130, 150, 160, 180, 200, 220, 240, 270, 300, 330, 360, 390, 430, 470, 510, 560, 620, 680, 750, 820, 910
    ),
    'E48': (
        100, 105, 110, 115, 121, 127, 133, 140, 147, 154, 162, 169, 178, 187, 196, 205, 215, 226, 237, 249, 261, 274, 287, 301, 316, 332, 348, 365, 383, 402, 422, 442, 464, 487, 511, 536, 562, 590, 619, 649, 681, 715, 750, 787, 825, 866, 909, 953
    ),
    'E96': (
        100, 102, 105, 107, 110, 113, 115, 118, 121, 124, 127, 130, 133, 137, 140, 143, 147, 150, 154, 158, 162, 165, 169, 174, 178, 182, 187, 191, 196, 200, 205, 210, 215, 221, 226, 232, 237, 243, 249, 255, 261, 267, 274, 280, 287, 294, 301, 309, 316, 324, 332, 340, 348, 357, 365, 374, 383, 392, 402, 412, 422, 432, 442, 453, 464, 475, 487, 499, 511, 523, 536, 549, 562, 576, 590, 604, 619, 634, 649, 665, 681, 698, 715, 732, 750, 768, 787, 806, 825, 845, 866, 887, 909, 931, 953, 976
    )
}
percent = {'E6': 0.2, 'E12': 0.1, 'E24': 0.05, 'E48': 0.02, 'E96': 0.01}
def pick_resistors(num: int) -> dict | None:
    nominals_dict = {}
    for nominal in nominals:
        nominals_dict[nominal] = calc(num, percent[nominal], nominals[nominal])
    if 100 <= num <= 999:
        return nominals_dict
    else:
        return None
        
def calc(num: int, nom_percent: float, nominal: str) -> tuple:
    """ Находит номинал с наименьшим отклонением от заданных отклонений """
    num1 = num-num*nom_percent
    num2 = num+num*nom_percent
    min_diff1 = min([abs(num1-i) for i in nominal])
    min_diff2 = min([abs(num2-i) for i in nominal])

    if 100 < num1 > 999:
        min_diff = min_diff2
    elif 100 < num2 > 999:
        min_diff = min_diff1
    else:
        min_diff = min([min_diff1, min_diff1])
        
    nom1 = filter(lambda x: abs(x-num1)==min_diff, nominal)
    nom2 = filter(lambda x: abs(x-num2)==min_diff, nominal)
    return tuple(nom1)+tuple(nom2)
  
# >>> pick_resistors(369)
# {'E6': (330,), 'E12': (330,), 'E24': (360,), 'E48': (365,), 'E96': (365,)}  

# >>> pick_resistors(190)
# {'E6': (150,), 'E12': (180,), 'E24': (180, 200), 'E48': (187,), 'E96': (187,)}