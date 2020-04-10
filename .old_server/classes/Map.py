from dataclasses import dataclass
from typing import Tuple, List
from classes.Column import Column

@dataclass
class Map:
    id: int
    size: Tuple[int,int]
    positions: List[List[Column]]