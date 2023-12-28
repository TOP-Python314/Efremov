def countable_nouns(num: int, word_ending: tuple[str, str, str]) -> str:
    if num in range(11, 21) or num%10 in [0, 5, 6, 7, 8, 9]:
        return word_ending[2]
    elif num%10 == 1:
        return word_ending[0]
    else:
        return word_ending[1]
        
# >>> countable_nouns(341, ("маска", "маски", "масок"))
# 'маска'

# >>> countable_nouns(0, ("маска", "маски", "масок"))
# 'масок'

# >>> countable_nouns(573, ("маска", "маски", "масок"))
# 'маски'