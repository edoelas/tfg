# pyright: strict

from classes.Position import Position
from classes.Entity import Entity
from typing import List, Dict

class Map:
    """A simple example class"""
    def __init__(self):
        self.width: int
        self.height: int
        self.entity_matrix: List[List[int]]
        self.entity_table: Dict[int,Entity] = dict()


    def load_map(self, width: int, height: int):
        self.entity_matrix = [[0 for x in range(width)] for y in range(height)]
        self.height = height
        self.width = width

    def update_entity(self,entity: Entity,new_pos: Position):
        self.entity_matrix[entity.position.y][entity.position.x] = 0
        self.entity_matrix[new_pos.y][new_pos.x] = entity.id

    def add_entity(self,entity: Entity):
        self.entity_matrix[entity.position.y][entity.position.x] = entity.id
        self.entity_table[entity.id] = entity

    def serialize(self):
        data = []
        for row in self.entity_matrix:
            json_row = []
            for val in row:
                if val == 0:
                    json_row.append({})
                else:
                    json_row.append(self.entity_table[val].serialize())

            data.append(json_row )
        
        return data

    def __str__(self):
        #TODO: arreglar esto con el nuevo planteamiento de una sola matriz
        ret: str = ""
        for y in range(self.height):
            for x in range(self.width):
                if 0 < self.entity_matrix[y][x] < 64 :
                    # ES JUGADOR
                    # esto es para que quede bonito
                    if self.entity_matrix[y][x] < 10:
                        ret += ' ' + str(self.entity_matrix[y][x])
                    else:
                        ret += str(self.entity_matrix[y][x])
                elif self.entity_matrix[y][x] != 0:
                    # ES ENTIDAD PERO NO JUGADOR
                    ret += '▓▓'
                else:
                    ret +='[]'
            ret += '\n'
        return ret