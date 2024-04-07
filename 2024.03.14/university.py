from enum import Enum
from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import date
from decimal import Decimal
from typing import Self

@dataclass        
class Contact:
    """ Контактные данные """    
    mobile: str = None
    email: str = None
    web: str = None
    telegram: str = None
    
@dataclass    
class PersonDate:
    """ Личные данные """
    last_name: str = None,
    first_name: str = None,
    patr_name: str = None,
    birthdate: str = None
    
class Person(ABC):
    """ Человек """
    def __init__(
            self,
            person_date: PersonDate = None,
            contact: Contact = None,
    ):
        self.person_date = PersonDate
        self.contact = Contact

    def __repr__(self):
        fn = self.person_date.__dict__['first_name']
        ln = self.person_date.__dict__['last_name']
        pn = self.person_date.__dict__['patr_name']
        return f'{self.__class__.__name__} --- id={id(self)} --- ({ln} {fn[0]}.{pn[0]}.)'
    
class Employer(Person):
    """ Сотрудник """
    def __init__(
            self,
            person_date: PersonDate = None,
            contact: Contact = None,
            position: str = None,
            income: Decimal = 1,
    ):
        super().__init__(person_date, contact)
        self.position = position
        self.income = income

class Student(Person):
        """ Студент """
        
        class EducationForm(Enum):
            """ Форма обучения """
            INTRAMURAL = 'очная'
            EXTRAMURAL = 'заочная'
            REMOTE = 'удаленная'
            
            def __repr__(self):
                return f'{self.__dict__['_value_']}'
        class ContractForm(Enum):
            """ Форма договора """
            BUDGET = 'бюджетный'
            COMPANY = 'целевой'
            PERSONAL = 'персональный'
            
        def __init__(
                self,
                person_date: PersonDate = None,
                contact: Contact = None,
                form: EducationForm = EducationForm.INTRAMURAL,
                contract: ContractForm = ContractForm.BUDGET,
                semester: int = 1,
                stipendia: Decimal = 1
        ):
            super().__init__(person_date, contact)
            self.id_ = str(id(self))
            self.form = form
            self.contract = contract
            self.semester = semester
            self.gradebook = Gradebook()
            self._stipendia = stipendia
            
        def stipendia(self, new_stipendia) -> None:
            """ Стипендия - setter """
            self._stipendia = new_stipendia
            stipendia = property(fset = stipendia)
            
class Teacher(Employer):
        """ Преподаватель """
        class Degree(Enum):
            """ Ученая степень """
            CANDIDATE = 'кандидат'
            DOCTOR = 'доктор'
            
            def __repr__(self):
                return f'{self.__dict__["_value_"]}'
                
        def __init__(
                self,
                person_date: PersonDate = None,
                contact: Contact = None,
                position: str = None,
                income: str = 1, 
                courses: list[str] = [],
                degree: Degree = Degree.CANDIDATE,
                professor: bool = False
        ):
            super().__init__(person_date, contact, position, income)
            self.courses = courses
            self.degree = degree
            self.professor = professor
        
class Administrator(Employer):
    """ Администратор """
    def __init__(
        self,
        person_date: PersonDate = None,
        contact: Contact = None,
        position: str = None,
        income: str = 1, 
        head: Self = None,
        subordinates: list[Employer] = []
    ):
        super().__init__(person_date, contact, position, income)
        self.head = head
        self.subordinates = subordinates
        
class Gradebook(dict):
    """ Зачетная книжка """
    @dataclass
    class GradeRecord:
        """ Запись в зачетку """
        class ExamType(Enum):
            
            CHECK = 'зачёт'
            DIFF_CHECK = 'дифзачёт'
            EXAMEN = 'экзамен'
            PROJECT = 'проект'
            
        semester: int = None
        date: date = None
        _type: ExamType = ExamType.CHECK
        grade: int = None
        scale: int = 5
        examiner: Teacher = None
    
    def __init__(self, records: dict[str, GradeRecord] = {}):
        self.id_ = str(id(self))
        self.records = records

class Group(list):
    """ Группа с учащимися """
    def __init__(
            self,
            id_: str = '',
            chief: Student = None,
            curator: Teacher = None,
    ):
        self.id_ = str(id(self))
        self.chief = chief
        self.curator = curator

@dataclass
class Auditorium:
    """ Аудитория """
    number: str = ''
    seats: int = 0
    building: str = 0

class OrganizationLvl(list):
    """ Организационный уровень """
    def __init__(
            self,
            title: str,
            description: str = '',
            head: Administrator = None,
            staff: list[Administrator] = [],
            contact: Contact = None
    ):
        super().__init__()
        self.title = title
        self.description = description
        self.head = head
        self._staff = staff
        self.contact = contact
 
    @property
    def staff(self) -> list:
        return self._staff
        
    @staff.setter
    def staff(self, human):
        self._staff.append(human)
    
    def __repr__(self):
        return f'{self.title}'
        
class Departament(OrganizationLvl):
    """ Кафедра """
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = [],
            contact = None,
            teachers: list[Teacher] = [],
            auditoria: list[Auditorium] = []
    ):
        super().__init__(title, description, head, staff, contact)
        self.teachers = teachers
        self.auditoria = auditoria
        
class Faculty(OrganizationLvl):
    """ Факультет """
    def __init__(
            self,
            title,
            description = None,
            head = None,
            staff = [],
            contact = None,
            departments: list[Departament] = []
    ):
        super().__init__(title, description, head, staff, contact)
        self.departments = departments
        
class University(OrganizationLvl):
    """ Университет """
    def __init__(
            self,
            title,
            description = None,
            head = None,
            _staff = [],
            contact = None,
            facultets: list[Faculty] = [],
    ):
        super().__init__(title, description, head, _staff, contact)
        self.facultets = facultets

    def change_head(self, person: Administrator) -> None:
        """ Выбрать управляющего """
        self.head = person