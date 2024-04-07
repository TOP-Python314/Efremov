from random import sample, choice, randint
from datetime import date
from data import HUMANS, SyktGU

from tester import Contact, Person, PersonDate, Employer, Teacher, Administrator, Student, Gradebook
from university import OrganizationLvl, Group, Auditorium, Faculty, Departament, University

def random_person():
    """ Выводит ФИО случайного человека """
    return choice(HUMANS).split(' ')

# >>> rp = random_person()
# >>> rp
# ['Белозеров', 'Александр', 'Потапович']    

def test_person_date(person):   
    """ Создает случайные личные данные """
    first_name = person[0]
    last_name = person[1]
    patr_name = person[2]
    birthday = f'{randint(1, 28)}.{randint(1, 12)}.{randint(1975, 2005)}'
    return PersonDate(first_name, last_name, patr_name, birthday)
    
# >>> tpd = test_person_date(rp)
# >>> for i in tpd.__dict__.items():
# ...     print(i)
# ...
# ('last_name', 'Белозеров')
# ('first_name', 'Александр')
# ('patr_name', 'Потапович')
# ('birthdate', '7.2.1980')

def test_contact(person=None):
    """ Создает случайные контактные данные """
    birthday = f'{randint(1975, 2005)}'
    mobile: str = f'+79{randint(100000000, 999999999)}'
    if person == None:
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        email: str =  f'{''.join(choice(letters) for _ in range(randint(5, 10)))}@{choice(['mail', 'gmail', 'icloud'])}.{choice(['ru', 'com', 'uk', 'io'])}'
        web: str = f'www.{''.join(choice(letters) for _ in range(randint(5, 8)))}.{choice(['ru', 'com', 'uk', 'io'])}'
        telegram: str = f'@{''.join(choice(letters) for _ in range(randint(3, 10)))}'
    else:
        email: str =  f'{person[1]}.{birthday}@{choice(['mail', 'gmail', 'icloud'])}.{choice(['ru', 'com', 'uk', 'io'])}'
        web: str = f'www.{person[1][:3]}{person[0][:3]}.{choice(['ru', 'com', 'uk', 'io'])}'
        telegram: str = f'@{person[0][:2]}{person[1][:2]}{person[2][:2]}{randint(1, 666)}'
    return Contact(mobile, email, web, telegram)
    
# >>> tc = test_contact(rp)
# >>> for i in tc.__dict__.items():
# ...     print(i)
# ...
# ('mobile', '+79894846815')
# ('email', 'Александр.1984@icloud.io')
# ('web', 'www.АлеБел.io')
# ('telegram', '@БеАлПо37')

# tc1 = test_contact()
# >>> for i in tc1.__dict__.items():
# ...     print(i)
# ...
# ('mobile', '+79392756838')
# ('email', 'ltjmss@icloud.ru')
# ('web', 'www.lkpfjrsj.ru')
# ('telegram', '@zmgvlozvd')

def test_person():
    """ Собирает и выводит данные человека """
    rp = random_person()
    person = Person()
    person.person_date = test_person_date(rp)
    person.contact = test_contact(rp)
    return person

# >>>tp = test_person()
# >>> for i in tp.__dict__.items():
# ...     if i[0] == 'person_date' or 'contact':
# ...             print(*i[1].__dict__.items(), sep='\n')
# ...
# ('last_name', 'Полоскун')
# ('first_name', 'Енот')
# ('patr_name', 'Лесович')
# ('birthdate', '2.11.1998')
# ('mobile', '+79449579566')
# ('email', 'Енот.1987@icloud.uk')
# ('web', 'www.ЕноПол.uk')
# ('telegram', '@ПоЕнЛе500')    

def test_student():
    """ Создает студента """
    student = Student()
    rp = random_person()
    student.person_date = test_person_date(rp)
    student.contact = test_contact(rp)
    return student

# >>> ts = test_student()
# >>> print(*ts.__dict__.items(), sep='\n')
# ('person_date', PersonDate(last_name='Полищук', first_name='Елизавета', patr_name='Владимировна', birthdate='23.8.1980'))
# ('contact', Contact(mobile='+79985519914', email='Елизавета.1978@mail.com', web='www.ЕлиПол.uk', telegram='@ПоЕлВл491'))
# ('id_', '1777117243936')
# ('form', очная)
# ('contract', <ContractForm.BUDGET: 'бюджетный'>)
# ('semester', 1)
# ('gradebook', {})
# ('_stipendia', 1)  
 
def test_teacher():
    """ Создает учителя """
    teacher = Teacher()
    rp = random_person()
    teacher.person_date = test_person_date(rp)
    teacher.contact = test_contact(rp)
    return teacher

# >>> tt = test_teacher()
# >>> print(*tt.__dict__.items(), sep='\n')
# ('person_date', PersonDate(last_name='Биба', first_name='Татьяна', patr_name='Николаевна', birthdate='26.12.1976'))
# ('contact', Contact(mobile='+79556890829', email='Татьяна.1989@mail.io', web='www.ТатБиб.com', telegram='@БиТаНи492'))
# ('position', None)
# ('income', 1)
# ('courses', [])
# ('degree', кандидат)
# ('professor', False)
    
def test_administrator():
    """ Создает администратора """
    admin = Administrator()
    rp = random_person()
    admin.person_date = test_person_date(rp)
    admin.contact = test_contact(rp)
    return admin
    
# >>> print(*ta.__dict__.items(), sep='\n')
# ('person_date', PersonDate(last_name='Птах', first_name='Валерия', patr_name='Эдуардовна', birthdate='24.5.1994'))
# ('contact', Contact(mobile='+79286714477', email='Валерия.1989@gmail.uk', web='www.ВалПта.uk', telegram='@ПтВаЭд381'))
# ('position', None)
# ('income', 1)
# ('head', None)
# ('subordinates', [])
    
def test_group():
    """ Создает группу с учениками """
    group = Group()
    group.curator = test_teacher()
    for _ in range(randint(15,20)):
        group.append(test_student())
    group.chief = choice(group)
    return group

# >>> tg = test_group()
# >>> print(*tg, sep='\n')
# Student (Попова В.В.) id=2999887549200
# Student (Клон З.С.) id=2999887604256
# Student (Ковальчук В.В.) id=2999887604064
# Student (Римских Л.С.) id=2999887603872
# Student (Птах В.Э.) id=2999887603632
# Student (Белозеров А.П.) id=2999887603248
# Student (Плакса С.А.) id=2999887604640
# Student (Патсак С.В.) id=2999887604784
# Student (Гербер Ф.В.) id=2999887605024
# Student (Клон З.С.) id=2999887605168
# Student (Полищук Е.В.) id=2999887605312
# Student (Ефремов Н.Д.) id=2999887605456
# Student (Ботан Д.К.) id=2999887605600
# Student (Арт Д.П.) id=2999887605744
# Student (Полищук Е.В.) id=2999887605888
# Student (Птах В.Э.) id=2999887606080
# Student (Марко Э.Г.) id=2999887606176
# Student (Потак К.А.) id=2999887606320
# >>>
# >>> print(*tg.__dict__.items(), sep='\n')
# ('id_', '2999887583568')
# ('chief', Student (Птах В.Э.) id=2999887603632)
# ('curator', Teacher (Литвинюк Н.В.) id=2999885285952)

    
def test_auditoriums():
    """ Создает аудиторию """
    auditoriums = []
    
    for n in range(50):
        seats = choice([25, 50, 100, 200])
        building = randint(1, 5)
        auditoriums.append(Auditorium(str(n), seats, f'Корпус-{building}'))
    return auditoriums

# >>> taud = test_auditoriums()
# >>> print(*taud, sep='\n')
# Auditorium(number='0', seats=200, building='Корпус-1')
# Auditorium(number='1', seats=200, building='Корпус-3')
# Auditorium(number='2', seats=25, building='Корпус-3')
# Auditorium(number='3', seats=25, building='Корпус-1')
# Auditorium(number='4', seats=200, building='Корпус-2')
# Auditorium(number='5', seats=50, building='Корпус-4')    
# ...
# Auditorium(number='44', seats=100, building='Корпус-5')
# Auditorium(number='45', seats=200, building='Корпус-1')
# Auditorium(number='46', seats=25, building='Корпус-2')
# Auditorium(number='47', seats=50, building='Корпус-2')
# Auditorium(number='48', seats=50, building='Корпус-2')
# Auditorium(number='49', seats=100, building='Корпус-4')

def test_university():
    """ Создает организацию университета """
    university = University('SyktGU')
    for key, value in SyktGU.items():
        faculty = Faculty(key)
        faculty.head = test_administrator()
        faculty.staff.append(faculty.head)
        faculty.contact = test_contact()
        faculty.departments = list(Departament(dep) for dep in SyktGU[key])
        for dep in faculty.departments:
            dep.head = test_administrator()
            dep.contact = test_contact()
            dep.teachers = list(test_teacher() for _ in range(10))
            for teacher in dep.teachers:
                teacher.contact = test_contact()
            dep.auditoria = choice(test_auditoriums())
        university.facultets.append(faculty)
    
    return university

# >>> print(*tu.__dict__.items(), sep='\n')
# ('title', 'SyktGU')
# ('description', None)
# ('head', None)
# ('_staff', [])
# ('contact', None)
# ('facultets', [Институт гуманитарных наук, Институт естественных наук, Институт иностранных языков, Институт истории и права, Институт культуры и искусства, Медицинский институт, Институт экономики и управления])

