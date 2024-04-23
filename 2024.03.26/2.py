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
    
    def __init__(self, name: str, text: str, **list_values: list):
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
        result = f"{margin}<{self.name}{vals}> {self.text} "
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
    def __init__(
            self, 
            root: HTMLTag, 
            *, 
            parent: Self = None
    ):
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
    
    def nested(self, name: str, text: str = '', **list_values: list) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, text, **list_values)
        self.root.add_nested_tag(tag)
        return HTMLBuilder(tag, parent=self)
    
    def sibling(self, name: str, text: str = '', **list_values: list) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, text, **list_values)
        self.root.add_nested_tag(tag)
        return self
    
    def closest(self) -> Self:
        """Возвращает строитель родительского тега относительного текущего тега"""
        if not self.__parent:
            return self
        else:
            return self.__parent
            
    def build(self) -> HTMLTag:
        """Возвращает корневой тег старшего строителя."""
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()



if __name__ == '__main__':
    
    # root = HTMLBuilder('div')
    html = HTMLTag.create('html')\
    .nested('body', 'Main', bg='yellow', font='sans')\
    .nested('header', bg='green', fontsize='100px')\
    .nested('div', border='10px sold white')\
    .nested('ul')\
    .sibling('li', 'text_1', color='grey', id='welcom')\
    .sibling('li', 'text_2', color='blue')\
    .closest()\
    .nested('ul')\
    .sibling('li', 'text_3', color='green')\
    .sibling('li', 'text_4', color='yellow')\
    .closest()\
    .closest()\
    .build()
    print(html)
    
# <html>
  # <body bg=yellow, font=sans> Main
    # <header bg=green, fontsize=100px>
      # <div border=10px sold white>
        # <ul>
          # <li color=grey, id=welcom> text_1 </li>
          # <li color=blue> text_2 </li>
        # </ul>
        # <ul>
          # <li color=green> text_3 </li>
          # <li color=yellow> text_4 </li>
        # </ul>
      # </div>
    # </header>
  # </body>
# </html> 