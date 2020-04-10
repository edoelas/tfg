# pyright: strict

class Client:
    def __init__(self, ip: str, port: int):
        self.IP: str = ip
        self.PORT: int = port
