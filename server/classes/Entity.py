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
        self.name: str = name
        self.max_health: int= max_health
        self.max_mana = 0
        self.mana = 0
        self.team: int = team
        self.__health: int = max_health
        self.possible_actions: List[ActionType] = possible_actions
        self.action_buffer: List[Action] = []
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
        self.action_buffer.append(action)
        
    def execute_action(self) -> None:
        action = self.action_buffer.pop(0)
        action.execute()

    def serialize(self):
        possible_action_list_id = []
        for action_type in self.possible_actions:
            possible_action_list_id.append(action_type.id)
        
        taken_action_list_id = []
        for action in self.action_buffer:
            action_id = [action.action_type.id,action.target_position.x,action.target_position.y]
            taken_action_list_id.append(action_id)
        
        return {		
            "name": self.name,
            "ID": self.id,
            "team": self.team,
            "health": self.health,
            "max_health": self.max_health,
            "mana": self.mana,
            "max_mana": self.max_mana,
            "possible_actions": possible_action_list_id,
            "taken_actions": taken_action_list_id
        }

    def __str__(self):
        string = "ID: " + str(self.id) + "\n" \
            "Name: " + self.name + "\n" \
            "Max health: " + str(self.max_health) + "\n" \
            "Health: " + str(self.health) + "\n" \
            "Max mana: " + str(self.max_mana) + "\n" \
            "Mana: " + str(self.mana) + "\n" \
            "Team: " + str(self.team) + "\n" \
            "Position: "  + str(self.position) + "\n" \
            "Possible actions: " + str([str(item) for item in self.possible_actions]) + "\n" \
            "Action buffer: " + str([str(item) for item in self.action_buffer]) + "\n" \
            "Client: " + str(self.client) + "\n" \
            
        return string
