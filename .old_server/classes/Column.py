from dataclasses import dataclass
from typing import Tuple, List

@dataclass
class Column:
    position: Tuple[int,int]
    height: int
    entity_list: List[int]