from classes.helpers import Address, Space
from classes.Entity import Entity
from dataclasses import dataclass

@dataclass
class Player:
    address: Address
    name: str
    entity: Entity
