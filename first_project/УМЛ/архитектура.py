@startuml  

interface dict
interface DictOfRanges {
    <font size=12>{(int, int): Any}</font>
    __init__()
    __getitem__()
}
class Kind {
    <font size=12>{(int, int): MaturePhase}</font>
    name: <i>str</i>
}

class MaturePhase{
    +params: <i>list </i>[Parameter]
}

class KindeParameter{
    +min: <i>float</i>
    +max: <i>float</i>
    +delata: <i>float</i>
}
class Creature {
    +kind: Kind
    +age: <i>int</i>
    +params: <i>dict</i> [<i>Type</i>, Parameter]
    --<font size=12><i> getters </i></font>--
    +age → <i>float</i>
    --<font size=12><i> setters </i></font>--
    +age()
    --<font size=12><i> methods </i></font>--
    -grow_up()
}

abstract Parameter {
    +{static}name: <i>str</i>
    -min: <i>float</i>
    -max: <i>float</i>
    #value: <i>float</i>  
    -delta: <i>float</i>
    --<font size=12><i> getters </i></font>--
    +value → <i>float</i>
    +range → <i>tuple</i> [<i>float</i>, <i>float</i>]
    --<font size=12><i> setters </i></font>--
    +value()
    --<font size=12><i> methods </i></font>--
    +{abstract}update()

}

class Health {
    +{abstract}update()
}

class Mood {
    +{abstract}update()
}
  
class Hunger {
        +{abstract}update()
}
class Thirst {
    +{abstract}update()
}
class Hygiene {
    +{abstract}update()
}

class Strength {
    +{abstract}update()
}

class Dexterity {
    +{abstract}update()
}

class Intelligence {
    +{abstract}update()
}

hide abstract empty members
hide class empty members
hide interface empty members

dict <-- DictOfRanges
DictOfRanges <-- Kind
Kind o-- MaturePhase
MaturePhase o-right- KindeParameter

Creature o-right- Parameter
Creature o-left- Kind
Parameter <|-- Health
Parameter <|-- Mood

Parameter <|-- Strength
Parameter <|-- Dexterity
Parameter <|-- Intelligence

Parameter <|-- Hunger
Parameter <|-- Thirst
Parameter <|-- Hygiene
@enduml