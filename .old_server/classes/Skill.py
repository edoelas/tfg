from dataclasses import dataclass
from classes.Map import Map
from abc import ABC, abstractmethod
from classes.helpers import Area, Shape

@dataclass
class Skill(ABC):
    '''
    Con la creación del personaje se instancia la clase. Cada invocación
    de la Skill es una llamada al metodo action()
    '''
    # TODO: forzar que estos atributos se sobrescriban
    # TODO: hay alguna forma de no tener que volver a indicar los tipos? -> pregutar stack
    id: int
    range: Area
    damage_amount: int  # negativo en el caso de que sane
    damage_area: Area 
    pasive: bool

    @abstractmethod
    def action(self, map: Map,pos_x: int, pos_y: int) -> None:
        pass

@dataclass
class Move(Skill):
    id : int = 3
    range: Area = Area(1,1,Shape.CROSS)
    damage_amount: int = 0
    damage_area: Area = Area(0,0,Shape.NONE)
    pasive: bool = False

    def action(self, map: Map,pos_x: int, pos_y: int) -> None:
        #TODO
        pass

@dataclass
class Throw(Skill):
    '''hace daño en area'''
    id: int = 1
    range: Area = Area(3,4,Shape.CROSS)
    damage_amount : int = 2
    damage_area : Area = Area(0,1,Shape.CROSS)
    pasive : bool = False

    def action(self, map: Map,pos_x: int, pos_y: int) -> None:
        # TODO
        pass

@dataclass
class Strike(Skill):
    '''Ataca a casillas adyacentes'''
    id: int = 2
    range: Area = Area(1,1,Shape.CROSS)
    damage_amount : int = 2
    damage_area : Area = Area(0,0,Shape.NONE)
    pasive : bool = False

    def action(self, map: Map,pos_x: int, pos_y: int) -> None:
        #TODO
        pass

@dataclass
class SummonHealFlor(Skill):
    '''Crea una entidad del tipo ProtectTile en la posicion indicada'''
    id : int = 4
    range : Area = Area(2,3,Shape.CROSS)
    damage_amount : object = None
    damage_area : Area = Area(0,0,Shape.NONE)
    pasive : bool = False

    def action(self, map: Map,pos_x: int, pos_y: int) -> None:
        #TODO
        pass

@dataclass
class HealFloorSkill(Skill):
    '''Cura a la persona que se encuentra sobre la casilla en cada turno'''
    id : int = 5
    range : None = None
    damage_amount : int = -2
    damage_area : Area = Area(0,0,Shape.NONE)
    pasive : bool = True

    def action(self, map: Map, pos_x: int, pos_y: int) -> None:
        #TODO
        pass