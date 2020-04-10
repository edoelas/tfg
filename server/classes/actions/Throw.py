# pyright: strict

from classes.Map import Map
from classes.Position import Position
from classes.Entity import Entity
from classes.ActionType import ActionType
from classes.Area import Area
from classes.AreaShape import AreaShape

class Throw(ActionType):
    def __init__(self):
        self.emiting_area: Area = Area(2,3,AreaShape.NORM1)
        self.receiving_area: Area = Area(0,1,AreaShape.CROSS)

    def execute(self,emitter: Entity,target_position: Position, map: Map) -> bool:
        if self.emiting_area.in_area(emitter.position, target_position):
            entities = self.receiving_area.get_entities_in_area(map,target_position)
            for entitie in entities:
                entitie.health -= 5
            return True
        else:
            print("out of range")
            return False