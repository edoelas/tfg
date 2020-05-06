# pyright: strict

class Client:
    def __init__(self, ip: str, port: int):
        self.ip: str = ip
        self.port: int = port

    def __str__(self):
        return "( IP: " + self.ip + ", port: " + str(self.port) + ")"