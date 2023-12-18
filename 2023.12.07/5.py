word = input()
scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
scores_sum = 0
for letter in word:
    for i in scores_letters:
        if letter.upper() in scores_letters[i]:
            scores_sum += i
            break
        
print(scores_sum)

# Ввод 1:
    # щелкунчик
    
    # 26

