from classes.helpers import Address
from classes.Map import Map
from classes.Column import Column
from classes.Player import Player
from classes.Game import Game
from classes.Entity import HealFloor, Warrior

if __name__ == '__main__':
    
    a1 = Address("127.0.0.1 ", 3331)
    w1 = Warrior((0,0))
    p1 = Player(a1,"p1",w1)

    a2 = Address("127.0.0.1 ", 3332)
    w2 = Warrior((0,0))
    p2 = Player(a2,"p2",w2)

    hf1 = HealFloor((2,1))

    columnList = [
        [Column((0,0), 1, []), Column((1,0), 1,[]), Column((2,0), 1, [])],
        [Column((0,1), 1, []), Column((1,1), 2,[]), Column((2,1), 2, [])],
        [Column((0,2), 1, []), Column((1,2), 2,[]), Column((2,2), 2, [])],
    ]
    map = Map(1,(3,3),columnList)

    g1 = Game(map,[p1,p2],[w1,w2,hf1])

    print("\n")
    print(w1.skills[0].id)