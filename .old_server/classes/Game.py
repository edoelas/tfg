from classes.Entity import Entity
from dataclasses import dataclass
from typing import Dict,List
from classes.Map import Map
from classes.Player import Player

@dataclass
class Game:
    map: Map
    players: List[Player]
    entities: List[Entity]
