from dataclasses import dataclass

@dataclass
class Base:
    x: int
    y: int = 0

@dataclass
class C(Base):
    z: int = 10
    x = 15

c = C()

print(c.x)