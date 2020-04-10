from classes.actions.Heal import Heal
from classes.actions.Throw import Throw
from classes.Position import Position
from classes.Game import Game
from classes.Entity import Entity
from classes.Client import Client
from classes.Map import Map

from classes.actions.Move import Move
from classes.actions.Strike import Strike

if __name__ == "__main__":

    map1 = Map()

    ground_matrix = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,2,2],
        [0,0,2,1],
    ]

    entity_matrix = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    map1.load_map(ground_matrix,entity_matrix)

    client1 = Client("localhost",1000)
    action_list = [Move(),Strike(),Throw(), Heal()]
    entity1 = Entity("test",100,1,action_list,client1,Position(2,0),map1,1)
    entity2 = Entity("test",100,1,action_list,client1,Position(1,0),map1,3)
    entity3 = Entity("test",100,1,action_list,client1,Position(3,1),map1,4)

    game = Game("ip", 1000, "asd")


    print("-------")
    print(map1)
    print(entity1.health)
    print(entity2.health)
    print(entity3.health)

    position3 = Position(2,0)
    entity1.load_action(action_list[3],position3)
    entity1.execute_action()


    print("---------------")
    print(map1)
    print(entity1.health)
    print(entity2.health)
    print(entity3.health)
