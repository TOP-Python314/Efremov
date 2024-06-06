from pathlib import Path
from sys import path
from typing import Self

    
class HTMLTag:
    """
    Описывает HTML тег, который может содержать вложенные теги.
    Может быть инициализирован с помощью строителя.
    """
    default_indent_spaces: int = 2

    def __init__(self, name: str, value: str = '', **kwargs):
        self.name = name
        self.value = value
        self.attr = kwargs        
        self.__nested: list[HTMLTag] = []

    def nested(self, html_tag: Self):
        """Добавляет вложенный тег к текущему."""
        self.__nested.append(html_tag)

    def __str(self, indent_level: int) -> str:
        """Рекурсивно формирует строку с текущим и всеми вложенными тегами."""
        margin = ' ' * indent_level * self.default_indent_spaces
        eol = ''
        attr = ''
        if self.attr:
            attr = ' ' + ' '.join(f'{k}="{v}"' for k, v in self.attr.items())
        result = f"{margin}<{self.name}{attr}>{self.value}"
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
    def create(name: str, value: str = '', **kwargs):
        return HTMLBuilder(name, value, **kwargs)


class HTMLBuilder:
    """
    Предоставляет методы для пошаговой инициализации экземпляра HTMLTag.
    """
    def __init__(self, root: HTMLTag | str, value: str = '', *, parent: Self = None, **kwargs):
        if isinstance(root, HTMLTag):
            pass
        elif isinstance(root, str):
            root = HTMLTag(root, value, **kwargs)
        else:
            raise TypeError('use HTMLTag or str instance for root parameter')
        self.root: HTMLTag = root
        self.__parent: Self = parent

    def nested(self, name: str, value: str = '', **kwargs) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает строитель для вложенного тега."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested(tag)
        return HTMLBuilder(tag, parent=self)
        

    def sibling(self, name: str, value: str = '', **kwargs) -> Self:
        """Добавляет вложенный тег к текущему тегу и возвращает текущий строитель."""
        tag = HTMLTag(name, value, **kwargs)
        self.root.nested(tag)
        return self
        

    def build(self) -> HTMLTag:
        if self.__parent is None:
            return self.root
        else:
            return self.__parent.build()
            
    def __str__(self):
        return str(self.root)       
        
        

class CVBuilder:
   
    """Kласс строитель для генерации HTML документа"""
    
    def __init__(self, fio: str, age: int, field_of_employment: str, email: str):
        self.fio = fio
        self.age = age
        self.field_of_employment = field_of_employment
        self.projects: list[tuple[str, tuple]] = []
        self.contacts: dict[str, str] = {"email": email}
      
    def add_education(self, university: str, profession: str, year_end: int) -> Self:
        
        """Добавляет информацию об университете, профессии и годе окончания"""
        
        self.university = university
        self.profession = profession
        self.year_end = year_end
        return self

  
    def add_project(self, name: str, *images: str) -> Self:
        
        """Добавляет проект в список проектов"""
        
        self.projects += [(name, images)]
        return self


    def add_contact(self, name_contact: str, contact: str) -> Self:
       
        """Добавляет контакт в словарь контактов"""
       
        self.contacts |= [(name_contact, contact)]
        return self


    def build(self):

        html = HTMLBuilder("html")
        head = html.\
            nested("head").\
            sibling("meta", charset="utf-8").\
            sibling("meta", content="width=device-width, initial-scale=1.0").\
            sibling("title", f'Портфолио: {self.fio}')
        body = html.nested("body", style="margin-left:10px")

        div_about= body.nested("div", id="about").\
            sibling("h1", "Портфолио").\
            sibling("h2", f'{self.fio}', style="color:red").\
            sibling("p", f'{self.field_of_employment}, {self.age} года', style="color:blue")
            
        div_about.sibling("p", ', '.join(f'{k} : {v}' for k, v in self.contacts.items()), style="color:blue")

        if self.university:
           div_about.sibling("p", f'Образование: {self.university}, {self.profession}, {self.year_end}')

        if self.projects:
            for project in self.projects:
                div_image = div_about.nested("div", f"{project[0]}", style="margin-left:30px; text-decoration:underline")
                div_image = div_about.nested("br")
                if project[1]:
                    for image in project[1]:
                        div_image.nested("img", src=image, width="250px", height="250px")
                        div_image.nested("br")

                      
        return html
        

cv1 = CVBuilder('Башлыков Александр Владимирович', 45, 'Web-разработчик', email='bav@mail.ru')\
    .add_education('ШАГ-академия', 'Python - 328', 2023)\
    .add_contact('telegram', '@123456')\
    .add_contact('mobile', '9171234567')\
    .add_project('Разработка логотипа для компании по производству снеков','3.1.png')\
    .add_project('UI разработка для интернет-магазина для восковых дел мастеров','3.2.png')\
    .build()

print(cv1)        

(Path(path[0]) / '3.html').write_text(str(cv1), encoding='utf-8')
