from dataclasses import dataclass
from typing import Tuple, List
from classes.Skill import Skill,Move,SummonHealFlor,Strike,Throw,HealFloorSkill
from classes.helpers import Address, Space
@dataclass

#TODO: crear algo similar a una interfaz o clase abstracta
@dataclass
class Entity:
    #id: int
    #health: int
    position: Tuple[int,int]
    #skills: List[Skill]
    #space: Space

@dataclass
class Warrior(Entity):
    id = 1
    health = 10
    space = Space.MID
    skills = [Move(),SummonHealFlor(),Strike(),Throw()]

@dataclass
class HealFloor(Entity):
    id = 3
    health = None
    space = Space.FLOOR
    skills = [HealFloorSkill]

'''
La idea es que los distintos tiles sean destruibles, pero por ahora esto
no se va a implementar ya que no forma parte del MVP
@dataclass
class Tile(Entity):
    id = 2
    health = 5
    space = Space.ALL
    skills = []
'''