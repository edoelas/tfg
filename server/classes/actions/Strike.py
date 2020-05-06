# pyright: strict

from classes.Map import Map
from classes.Position import Position
from classes.Entity import Entity
from classes.ActionType import ActionType
from classes.Area import Area
from classes.AreaShape import AreaShape

class Strike(ActionType):
    def __init__(self):
        self.emiting_area: Area = Area(1,1,AreaShape.CROSS)
        self.receiving_area: Area = Area(0,0,AreaShape.NONE)
        self.id = 2

    def execute(self,emitter: Entity,target_position: Position, map: Map) -> bool:
        if self.emiting_area.in_area(emitter.position, target_position):
            entities = self.receiving_area.get_entities_in_area(map,target_position)
            for entitie in entities:
                entitie.health -= 10
            return True
        else:
            print("out of range")
            return False