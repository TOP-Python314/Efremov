""" Шаблоны проектирования """
"""Демонстратор строителя."""

from pathlib import Path
from sys import path
from typing import Self


class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2
    
    def __init__(self, name: str, *text: str, **list_values: list):
        self.name = name
        self.text = text
        self.list_values: dict = {str(key): str(value) for key, value in list_values.items()}
        self.__nested: list[HTMLTag] = []
    
    def add_nested_tag(self, html_tag: Self) -> None:
        """Добавляет вложенный тег к текущему."""
        self.__nested.append(html_tag)
    
    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        vals = f'{' ' if self.list_values else ''}'+', '.join([f'{key}={value}' for key, value in self.list_values.items()])
        text_in = ', '.join(self.text)
        result = f"{margin}<{self.name}{vals}> {text_in} "
        if self.__nested:
            for tag in self.__nested:
                result += '\n' + tag.__str(indent_level+1)
            eol = f'\n{margin}'
        result += f"{eol}</{self.name}>"
        return result
    
    def __str__(self):
        return self.__str(0)
    
    # в данной реализации нецелесообразно "прятать" класс HTMLBuilder
    @staticmethod
    def create(name: str, value: str = '') -> 'HTMLBuilder':
        return HTMLBuilder.with_tag(name, value)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', *, parent: Self = None, **kwargs):
        if isinstance(root, HTMLTag):
            pass
        elif isinstance(root, str):
            root = HTMLTag(root, *value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')
        self.root: HTMLTag = root
        self.__parent: Self = parent
    
    @classmethod
    def with_tag(
            cls, 
            name: str, 
            value: str = '', 
            *, 
            parent: Self = None
    ) -> Self:
        tag = HTMLTag(name, value)
        return cls(tag, parent=parent)
    
    def nested(self, name: str, *text: str, **list_values: list) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, *text, **list_values)
        self.root.add_nested_tag(tag)
        return HTMLBuilder(tag, parent=self)
    
    def sibling(self, name: str, *text: str, **list_values: list) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, *text, **list_values)
        self.root.add_nested_tag(tag)
        return self
    
    def build(self) -> HTMLTag:
        """Возвращает корневой тег старшего строителя."""
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()
            
    def __str__(self):
        return str(self.root)

class PortfolioBuilder:
        
    def __init__(self, fio: str, age: str, activity: str):
        self.fio = fio
        self.age = age
        self.activity = activity
        self.projects: dict[str, list(str, ...)] = {}
        self.contacts: dict[str, str] = {}
        self.education: list[list[str, str, str]] = []
        
    def add_education(self, university: str, profession: str, release: str) -> Self:
        self.education += [(university, profession, str(release))]
        return self
        
    def add_project(self, name: str, *slides: str) -> Self:
        self.projects |= [(name, slides)]
        return self
        
    def add_contact(self, name: str, contact: str):
        self.contacts |= [(name, contact)]
        return self 
        
    def build(self):
        
        html = HTMLBuilder('html')
        head = html.nested('head')\
                   .sibling('meta', charset="utf-8")\
                   .sibling('meta', content="width=device-width, initial-scale=1.0")\
                   .sibling('title', f'Портфолио: {self.fio}')
        
        body = html.nested('body', style="margin-left:10px")
        
        info = body.nested('p', id="about")\
               .sibling('h1', 'Портфолио')\
               .sibling('h2', f'{self.fio} {self.age} года', style="color:red")\
               .sibling('p', f'{self.activity}', style="color:blue")\
               .sibling('p', *(f'{i}: {j}' for i, j in self.contacts.items()), style='color: blue')
        
        if self.education:
            education_info = info.nested('p', 'Образоание:')
            for i in self.education:
                education_info.sibling('h4', f'Название учебного заведения: {i[0]}')\
                              .sibling('h4', f'Специальность: {i[1]}')\
                              .sibling('h4', f'дата выпуска: {i[2]}')\
                    
        if self.projects:
        
            for project in self.projects:
                block_project = info.nested('div', f'{project}')
                for img in self.projects[project]:
                    block_project.sibling('img', f'{img}')
        return html

cv1 = PortfolioBuilder('Ефремов Никита Дмитриевич', 32, 'Web-разработчик')\
    .add_education('ТОР-академия', 'Python314', 2024)\
    .add_education('SyktGU', 'Биология', 2014)\
    .add_contact('telegram', '@123456')\
    .add_contact('mobile', '9129344853')\
    .add_project('Разработка приложения по отслеживанию физико-морфологической изменчивости ихтиофауны заданного ареала','1.png','2.png')\
    .add_project('Разработка Web - ориентированного приложения для учебной организации в области ихтиологии', '3.png', '4.png', '5.png')\
    .build()

print(cv1)    
  
# <html>
  # <head>
    # <meta charset=utf-8>  </meta>
    # <meta content=width=device-width, initial-scale=1.0>  </meta>
    # <title> Портфолио: Ефремов Никита Дмитриевич </title>
  # </head>
  # <body style=margin-left:10px>
    # <p id=about>
      # <h1> Портфолио </h1>
      # <h2 style=color:red> Ефремов Никита Дмитриевич 32 года </h2>
      # <p style=color:blue> Web-разработчик </p>
      # <p style=color: blue> telegram: @123456, mobile: 9129344853 </p>
      # <p> Образоание:
        # <h4> Название учебного заведения: ТОР-академия </h4>
        # <h4> Специальность: Python314 </h4>
        # <h4> дата выпуска: 2024 </h4>
        # <h4> Название учебного заведения: SyktGU </h4>
        # <h4> Специальность: Биология </h4>
        # <h4> дата выпуска: 2014 </h4>
      # </p>
      # <div> Разработка приложения по отслеживанию физико-морфологической изменчивости ихтиофауны заданного ареала
        # <img> 1.png </img>
        # <img> 2.png </img>
      # </div>
      # <div> Разработка Web - ориентированного приложения для учебной организации в области ихтиологии
        # <img> 3.png </img>
        # <img> 4.png </img>
        # <img> 5.png </img>
      # </div>
    # </p>
  # </body>
# </html>
