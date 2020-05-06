## pyright: strict

from classes.Map import Map
from classes.Entity import Entity
from classes.Position import Position
from classes.Client import Client
from classes.actions.Move import Move
from classes.actions.Strike import Strike
from classes.actions.Throw import Throw
from classes.actions.Heal import Heal
from classes.Action import Action

from typing import List
import json

class Game:
    """A simple example class"""
    def __init__(self, ip: str, port: int):
        self.IP: str = ip
        self.PORT: int = port
        self.map: Map
        self.action_table = {
                        1:Move(),
                        2:Strike(),
                        3:Throw(),
                        4:Heal()
                    }

    def serialize_server(self):        
        return self.map.serialize()


    def unserialize_client(self, data_list: List):
        '''
        Recibe una lista de mensajes de distintos clientes
        '''
        for data in data_list:
            emitter_id = data[0]
            emitter = self.map.entity_table[emitter_id]
            emitter.action_buffer = []

            for data_action in data[1:]:
                action_type_id = data_action["action_type_id"]
                position = Position(data_action["pos"][0],data_action["pos"][1])
                action_type = self.action_table[action_type_id]
                action = Action(action_type,emitter, position, self.map)

                emitter.action_buffer.append(action)


    def load_game(self, game_data):
        self.map = Map()
        width = len(game_data[0])
        height = len(game_data)
        self.map.load_map(width,height)

        # Se debe de hacer en 2 pasos puesto que es necesario primero crear la matriz de
        # entidades y luego cargar las entidades
        # TODO?: crear load Entity
        for y in range(height):
            for x in range(width):
                if "ID" in game_data[y][x]:
                    json_entity = game_data[y][x]
                    name: str = json_entity["name"]
                    max_health: int = json_entity["max_health"]
                    team: int = json_entity["team"]
                    
                    possible_actions_id: List[int] = json_entity["possible_actions"]
                    possible_actions = []
                    for action_id in possible_actions_id:
                        possible_actions.append(self.action_table[action_id])
                        
                    client  = Client(json_entity["IP"],json_entity["port"])
                    position = Position(x,y)
                    id = json_entity["ID"]
                    # Las entidades se añaden automaticamente al mapa ser creadas
                    # Se asume que en la etapa de carga las entidades no han ejecutado ninguna accion
                    Entity(name, max_health, team, possible_actions, client,position,self.map,id)

