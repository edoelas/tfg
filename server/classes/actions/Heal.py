from classes.Map import Map
from classes.Position import Position
from classes.Entity import Entity
from classes.ActionType import ActionType
from classes.Area import Area
from classes.AreaShape import AreaShape


class Heal(ActionType):
    def __init__(self):
        self.emiting_area: Area = Area(0, 0, AreaShape.NONE)
        self.receiving_area: Area = Area(0, 0, AreaShape.CROSS)
        self.id = 4

    def execute(self, emitter: Entity, target_position: Position,
                map: Map) -> bool:
        if self.emiting_area.in_area(emitter.position, target_position):
            entities = self.receiving_area.get_entities_in_area(
                map, target_position)
            for entity in entities:
                entity.health += 3
            return True
        else:
            print("out of range")
            return False
