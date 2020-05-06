## pyright: strict

from classes.Position import Position
#from classes.Entity import Entity
from classes.ActionType import ActionType
#from classes.Map import Map

class Action:
    def __init__(self, action_type: ActionType, emiter,target_position: Position, map):
        self.action_type: ActionType = action_type
        self.emiter = emiter
        self.target_position: Position = target_position
        self.map = map

    def execute(self) -> None:
        self.action_type.execute(self.emiter,self.target_position, self.map)

    def __str__(self):
        return str(self.action_type) + "( " + str(self.target_position.x) + ", "+ str(self.target_position.x) +")"