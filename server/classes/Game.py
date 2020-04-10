# pyright: strict

from classes.Map import Map

class Game:
    """A simple example class"""
    def __init__(self, ip, port, map):
        self.IP: str = ip
        self.PORT: int = port
        self.map: Map = map


