from dataclasses import dataclass
from enum import Enum

@dataclass
class Shape(Enum):
    NONE = 1 # No se calcula el area, se asume que solo afecta a una casilla
    AREA = 2 # distancia 1-norm
    CROSS = 3 
    LINE = 4 # Pensada para el daño. Sol funciona con Skill cuya forma es tipo CROSS.
    SQUARE = 5 # La diagonal cuenta como 1 en la distancia

@dataclass
class Space(Enum):
    NONE = 1
    FLOOR = 2
    MID = 3 
    TOP = 4
    ALL = 5

@dataclass
class Area:
    '''La primera posición es cero. Ambas distancias se incluyen'''
    dist_min: int
    dist_max: int
    shape: Shape

@dataclass
class Address:
    ip: str
    port: int

