@startuml


abstract Person {
    +last_name: <i>str</i>
    +first_name: <i>str</i>
    +patr_name: <i>str</i>
    +birthdate: <i>date</i>
    +contact: Contact
}

class Contact << dataclass >> {
    +mobile: <i>str</i>
    +office: <i>str</i>
    +email: <i>str</i>
    +telegram: <i>str</i>
    +web: <i>str</i>
}

class Student {
    +id: <i>str</i>
    +form: EducationForm
    +contract: ContractForm
    #stipendia: <i>dec</i>
    +gradebook: Gradebook
    .. <font size=12><i> setters  </i></font> ..
    +set_stipendia()
}

enum EducationForm {
    INTRAMURAL
    EXTRAMURAL
    REMOTE
}

enum ContractForm {
    BUDGET
    COMPANY
    PERSONAL
}

abstract dict

class Gradebook {
    <font size=12><font "Space Mono"><i>str</i>: GradeRecord</font>
    --
    +id: <i>str</i>
    .. <font size=12><i> getters  </i></font> ..
    +average() → <i>float</i>
}

class GradeRecord << dataclass >> {
    +name: <i>str</i>
    +date: <i>date</i>
    +type: ExamType
    +semester: <i>int</i>
    +grade: <i>int</i>
    +scale: <i>int</i>
    +examiner: Teacher
}

enum ExamType {
    CHECK
    DIFF_CHECK
    EXAMEN
    PROJECT
}

abstract Employee {
    +position: <i>str</i>
    #income: <i>dec</i>
    +joined: <i>date</i>
    .. <font size=12><i> setters  </i></font> ..
    +set_income()
}

class Teacher {
    -previous_experience: <i>int</i>
    +courses: <i>list</i> [<i>str</i> ]
    +degree: Degree
    +professor: <i>bool</i>
    .. <font size=12><i> getters  </i></font> ..
    +total_experience() → <i>int</i>
    --
    +make_examination()
}

enum Degree {
    CANDIDATE
    DOCTOR
}

class Administrator {
    +subordinates: <i>list</i> [Employee]
}

Person <|--- Student
Person <|-- Employee

Employee <|-- Teacher
Employee <|-- Administrator
Employee --o Administrator

Person o-left- Contact

Teacher *-- Degree
Teacher --o GradeRecord
Teacher .left.> Gradebook : "GradeRecord()"

Student *-- EducationForm
Student *-- ContractForm
Student o-right- Gradebook

dict <|-- Gradebook

Gradebook *-- GradeRecord

GradeRecord *-left- ExamType

hide abstract empty members
hide enum empty members
hide Contact empty members
hide GradeRecord empty members

' Person -[hidden]- Teacher
Teacher -[hidden]right- Administrator
' Contact -[hidden]- EducationForm

@enduml