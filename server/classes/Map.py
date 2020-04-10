# pyright: strict

from classes.TerrainTypes import TerrainTypes
from classes.Position import Position
from classes.Entity import Entity
from typing import List, Dict

class Map:
    """A simple example class"""
    def __init__(self):
        self.width: int
        self.height: int
        self.ground_matrix: List[List[int]]
        self.entity_matrix: List[List[int]]
        self.entity_table: Dict[int,Entity] = dict()


    def load_map(self, ground_matrix: List[List[int]], entity_matrix: List[List[int]]):
        self.ground_matrix = ground_matrix
        self.entity_matrix = entity_matrix
        self.height = len(ground_matrix)
        self.width = len(ground_matrix[0])
        #TODO: anadir metodos para asegurarse que hambas matrices son
        # del mismo tamano y que son completamente cuadradas. En caso
        # contrario lanzar error 
        # Entity matrix debe ser una copia de la primera matriz de ceros

    def update_entity(self,entity: Entity,new_pos: Position):
        self.entity_matrix[entity.position.y][entity.position.x] = 0
        self.entity_matrix[new_pos.y][new_pos.x] = entity.id

    def add_entity(self,entity: Entity):
        self.entity_matrix[entity.position.y][entity.position.x] = entity.id
        self.entity_table[entity.id] = entity

    def __str__(self):
        ret: str = ""
        for y in range(self.height):
            for x in range(self.width):
                if self.ground_matrix[y][x] == TerrainTypes.WALL.value:
                    ret += '▢ '
                elif self.ground_matrix[y][x] == TerrainTypes.HOLE.value:
                    ret += '◉ '
                elif self.entity_matrix[y][x] != 0:
                    ret += str(self.entity_matrix[y][x]) + ' '
                else:
                    ret +='. '
            ret += '\n'
        return ret