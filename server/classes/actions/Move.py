# pyright: strict

from classes.Map import Map
from classes.Position import Position
from classes.Entity import Entity
from classes.ActionType import ActionType
from classes.Area import Area
from classes.AreaShape import AreaShape

class Move(ActionType):
    def __init__(self):
        self.emiting_area: Area = Area(1,1,AreaShape.CROSS)
        self.receiving_area: Area = Area(0,0,AreaShape.NONE)
        self.id = 1

    def execute(self,emitter: Entity,target_position: Position, map: Map) -> bool:
        if self.emiting_area.in_area(emitter.position, target_position):
            emitter.position = target_position
            return True
        else:
            print("out of range")
            return False