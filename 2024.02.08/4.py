from csv import reader, writer
from sys import path
from pathlib import Path

class CountableNouns:
    db_path: Path = Path(path[0]) / 'words.csv'
    words: dict[str, tuple[str, str]] = {}
    
    with open(db_path, encoding='utf-8') as dp:
        file_reader = reader(dp, delimiter = ",")
        words = {line[0]: tuple(line[1:]) for line in file_reader}
        
    @classmethod
    def save_words(cls, word1: str = None) -> None:
        """Метод запрашивает в stdin слова, добавляет их в words и дописывает в файл.
        
        :param word1: слово добавляемое в словарь words
        """
        new_words = ['один', 'два', 'пять']
        template = '    введите слово, согласующееся с числительным "{}": '
        
        if not word1:
            new_words = [input(template.format(nw)) for nw in new_words]
        else:
            new_words = [input(template.format(nw)) for nw in new_words[1:]]
            new_words.insert(0, word1)
        cls.words[new_words[0]] = tuple(new_words[1:])
        
        with open(cls.db_path, 'a', encoding='utf-8') as cdb:
            file_writer = writer(cdb, delimiter = ",", lineterminator='\n')
            file_writer.writerow(new_words)
        
    @classmethod
    def pick(cls, number: int, word: str) -> str:
        """Метод возвращает согласованное существительное с числом.
    
        :param number: число для согласования.
        :param word: существительное для согласования.
        :return: согласованное с числом существительное. 
        """
        
        if word not in cls.words:
            print(f'существительное "{word}" отсутствует в базе')
            cls.save_words(word)
            return None
        
        choice_words = word, *cls.words[word]
        last_digit = number % 10
        decade_digit = number % 100 // 10
        
        if decade_digit == 1 or last_digit > 4:
            return choice_words[2]
        if last_digit == 1:
            return choice_words[0]
        return choice_words[1]
        
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'ячейка': ('ячейки', 'ячеек')}
# >>>
# >>> CountableNouns.pick(12, 'год')
# 'лет'
# >>> CountableNouns.pick(365, 'день')
# 'дней'
# >>> CountableNouns.pick(1354, 'кирпич')
# существительное "кирпич" отсутствует в базе
    # введите слово, согласующееся с числительным "два": кирпича
    # введите слово, согласующееся с числительным "пять": кирпичей
# >>>
# >>> CountableNouns.words
# {'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'ячейка': ('ячейки', 'ячеек'), 'кирпич': ('кирпича', 'кирпичей')}
# >>>
# >>> CountableNouns.save_words()
    # введите слово, согласующееся с числительным "один": ветка
    # введите слово, согласующееся с числительным "два": ветки
    # введите слово, согласующееся с числительным "пять": веток
# >>>
# >>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
# год,года,лет
# месяц,месяца,месяцев
# день,дня,дней
# ячейка,ячейки,ячеек
# кирпич,кирпича,кирпичей
# ветка,ветки,веток