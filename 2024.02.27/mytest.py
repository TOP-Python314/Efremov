from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass
class Test:
    name: str = None,
    last_name: str = None,
    age: str = None
    
class Test2(ABC):
    def __init__(
            self,
            test: Test = None
    ):
        self.test = test
        self.name = test[name]
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'