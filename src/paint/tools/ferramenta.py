from abc import ABC, abstractmethod

class Ferramenta(ABC):

    @abstractmethod
    def clique(self, evento):
        pass

    @abstractmethod
    def arrastar(self, evento):
        pass

    @abstractmethod
    def soltar(self, evento):
        pass