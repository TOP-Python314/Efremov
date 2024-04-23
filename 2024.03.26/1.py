"""Демонстратор строителя."""

from pathlib import Path
from sys import path
from typing import Self
        
class ClassTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2
    
    def __init__(self, name: str, value: str = ''):
        self.name = name
        self.value = value
        self.__cls_atr: dict[ClassTag] = {}
        self.__init_param: dict[ClassTag] = {}
        
    def add_nested_tag(self, html_tag: Self) -> None:
        """ Добавляет вложенный тег к текущему """
        self.__nested.append(html_tag)
        
    def add_param(self, name: str, value: str) -> None:
        """ Добавляет в словарь поля класса """
        self.__cls_atr[name] = value
        
    def add_func_atr(self, name: str, value: str) -> None:
        """ Добавляет в словарь атрибуты экземпляра """
        self.__init_param[name] = value
        
    def __str(self, indent_level: int) -> str:
        
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        result = f"{self.name}\n"
        if not self.__cls_atr and not self.__init_param:
            result += '\n    pass'
        else:
            if self.__cls_atr:
                for key, value in self.__cls_atr.items():
                    result += f'\n    {key} = {value}'
            if self.__init_param:
                result += f'\n\n    def __init__(self):'
                for key, value in self.__init_param.items():
                    result += f'\n        self.{key} = {value}'
            
        return result
    
    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name: str, value: str = '') -> 'ClassBuilder':
        return ClassBuilder.with_tag(name, value)


class ClassBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(
            self, 
            root: ClassTag, 
            *, 
            parent: Self = None
    ):
        if isinstance(root, ClassTag):
            self.root = root
        elif isinstance(root, str):
            self.root = ClassTag(root)
        else:
            raise TypeError('use ClassBuilder or str instance for root parameter')

        self.root: ClassTag = root
        self.__parent: Self = parent
    
    @classmethod
    def with_tag(
            cls, 
            name: str, 
            value: str = '', 
            *, 
            parent: Self = None
    ) -> Self:
        tag = ClassTag(name, value)
        if value:
            value = f'({value})'
        tag.__dict__['name'] = f'class {tag.__dict__['name']}{value}:'
        
        return cls(tag, parent=parent)
        
    def class_field(self, name: str, value: str = ''):
        """ Добавляет в класс поля класса со значениями """
        self.root.add_param(name, value)
        return self
        
    def inst_attr(self, name: str, value: str = ''):
        """ Добавляет в конструктор атрибуты экземпляра со значениями """
        self.root.add_func_atr(name, value)
        return self
        
    def build(self) -> ClassTag:
        """Возвращает корневой тег старшего строителя."""
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()

test = ClassTag.create('Test_class')\
               .class_field('param_1', 'value_param_1')\
               .class_field('param_2', 'value_param_2')\
               .inst_attr('init_atr_2', [])\
               .inst_attr('init_atr_1', 14)\
               .build()
print(test)

# class Test_class:

    # param_1 = value_param_1
    # param_2 = value_param_2

    # def __init__(self):
        # self.init_atr_2 = []
        # self.init_atr_1 = 14