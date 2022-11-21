
# Adaptee (source) interface
class LightingPort:
    def voltage(self) -> int:
        pass

    def power(self) -> int:
        pass

    def live(self) -> int:
        pass


# Adaptee
class Port(LightingPort):
    def voltage(self) -> int:
        return 5

    def power(self) -> int:
        return 2.4

    def live(self) -> int:
        return 1

# Target interface
class TypeCPort:
    def voltage(self) -> int:
        pass

    def power(self) -> int:
        pass


# The Adapter
class Adapter(TypeCPort):
    __port = None

    def __init__(self, port) -> None:
        self.__port = port
    
    def voltage(self):
        return 3
    
    def live(self):
        return self.__port.live()


# Client
class Airpods:
    __power = None

    def __init__(self, power):
        self.__power = power

    def charge(self):
        if self.__power.voltage() > 3:
            print("Error! Incompatible charging ports.")
        else:
            if self.__power.live() == 1:
                print("Charging...")
            else:
                print("No Power.")