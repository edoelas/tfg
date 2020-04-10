## pyright: strict

from classes.ActionType import ActionType
#from classes.Map import Map
from classes.Position import Position
from classes.Client import Client
from classes.Action import Action
from typing import List

class Entity:
    """
    The entities are added from the Game object
    """
    def __init__(self, name: str, max_health: int,team: int,
    possible_actions: List[ActionType], client: Client,position: Position,map,id: int):
        self.__id: int = id
        #self.__name: str = name
        self.max_health: int= max_health
        self.team: int = team
        self.__health: int = max_health
        self.possible_actions: List[ActionType] = possible_actions
        self.__action_buffer: List[Action] = []
        self.client: Client = client
        self.__position: Position = position
        #Map is here in order to update it each time an entity moves
        self.map = map

        self.map.add_entity(self)


    @property
    def position(self) -> Position:
        return self.__position

    @position.setter
    def position(self, new_position: Position):
        self.map.update_entity(self,new_position)
        self.__position = new_position

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, new_health: int):
        if 0 <= new_health <= self.max_health :
            self.__health = new_health
        elif 0 > new_health:
            self.__health = 0
        elif self.max_health >= new_health:
            self.__health = self.max_health

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self,id: int):
        pass


    def load_action(self,actionType: ActionType,target_position: Position) -> None:
        action = Action(actionType, self,target_position,self.map)
        self.__action_buffer.append(action)
        
    def execute_action(self) -> None:
        action = self.__action_buffer.pop(0)
        action.execute()