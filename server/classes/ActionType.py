## pyright: strict

from abc import abstractmethod
#from classes.Map import Map
from classes.Position import Position
#from classes.Area import Area
#from classes.Entity import Entity

class ActionType:
    def __init__(self):
        raise NotImplementedError

    @property
    def emiting_area(self):
        return self.__emiting_area

    @emiting_area.setter
    def emiting_area(self, emiting_area) -> None:
        self.__emiting_area = emiting_area

    @property
    def receiving_area(self):
        return self.__receiving_area

    @receiving_area.setter
    def receiving_area(self, receiving_area) -> None:
        self.__receiving_area = receiving_area


    @abstractmethod
    def execute(self,emitter,target_position: Position, map) -> bool:
        raise NotImplementedError


