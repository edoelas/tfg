# pyright: strict

from __future__ import annotations

class Position:
    """A simple example class"""
    def __init__(self,x: int,y: int):
        self.x: int = x
        self.y: int = y

    def distance_to(self, position: Position ) -> None:
        pass

    def __str__(self):
        return str((self.x,self.y))