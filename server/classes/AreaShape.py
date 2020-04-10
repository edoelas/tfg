from enum import Enum

class AreaShape(Enum):
    NONE = 1 # No se calcula el area, se asume que solo afecta a una casilla
    NORM1 = 2 # distancia 1-norm
    CROSS = 3 
    LINE = 4 # Pensada para el daño. Sol funciona con Skill cuya forma es tipo CROSS.
    SQUARE = 5 # La diagonal cuenta como 1 en la distancia
