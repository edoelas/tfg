# pyright: strict

from classes.Entity import Entity
from classes.Position import Position
from classes.AreaShape import AreaShape
#from classes.Entity import Entity
from classes.Map import Map
from typing import Dict, List

class Area:
    def __init__(self, min_distance: int, max_distance: int, area_type: AreaShape):
        self.min_distance: int = min_distance 
        self.max_distance: int = max_distance
        self.area_type: AreaShape = area_type

    def in_area(self,center: Position, position: Position) -> bool:
        areas: Dict[AreaShape, bool] = { 
            AreaShape.NONE:
                center.x == position.x and center.y == position.y,
            AreaShape.CROSS:
                center.x == position.x and self.min_distance <= abs(center.y-position.y) <= self.max_distance or
                center.y == position.y and self.min_distance <= abs(center.x-position.x) <= self.max_distance,
            AreaShape.SQUARE:
                self.min_distance <= abs(center.x-position.x) <= self.max_distance and
                self.min_distance <= abs(center.y-position.y) <= self.max_distance,
            AreaShape.NORM1:
                self.min_distance <= (abs(center.x - position.x) + abs(center.y - position.y)) <= self.max_distance
        }

        return areas[self.area_type]


    def get_entities_in_area(self, map: Map, center: Position) -> List[Entity]:
        #TODO: esto es basura y se tiene que cambiar
        # Se puede hacer de forma sencilla recortando en forma de area cuadrada
        ret = []
        for y in range(map.height):
            for x in range(map.width):
                if self.in_area(center,Position(x,y)):
                    if map.entity_matrix[y][x] != 0:
                        entity = map.entity_table[map.entity_matrix[y][x]]
                        ret.append(entity)

        return ret
