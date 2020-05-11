from classes.actions.Heal import Heal
from classes.actions.Throw import Throw
from classes.Position import Position
from classes.Game import Game
from classes.Entity import Entity
from classes.Client import Client
from classes.Map import Map

import json
import os

from classes.actions.Move import Move
from classes.actions.Strike import Strike

##

 __name__ == "__main__":
    game = Game("localhost", 1234)
    with open('./games/g1.json') as g1:
        game_data = json.load(g1)
        game.load_game(game_data
        print(game.map.entity_table[1])

        with open('./client_messages/cm1.json') as cm1:
            client_actions_data = json.load(cm1)
            game.unserialize_client([client_actions_data])

            print(game.map.entity_table[1])
