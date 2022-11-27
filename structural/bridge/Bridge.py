from adapter.Adapter import *
from proxy.Proxy import *


class Component:
    def __str__(self) -> str:
        pass


class CPU(Component):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "A16"


class iOS(Component):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "iOS 14.1"


class AirpodsProMax(Airpods):
    def connect(self):
        print("Connecting to iPhone...")
        method = Bluetooth()
        method.connect()
