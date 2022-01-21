from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consuption(self):
        pass

    def __add__(self, other):
        return self.consuption + other.consuption

class Coat(Clothes):

    @property
    def consuption(self):
        return round(self.param / 6.5) + 0.5

class Costume(Clothes):
    @property
    def consuption(self):
        return (2 * self.param + 0.3) / 100


coat = Coat(58)
costume = Costume(240)
print (coat + costume)