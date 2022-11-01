from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_bmw(self) -> BMW:
        pass

    @abstractmethod
    def create_mercedes(self) -> Mercedes:
        pass


class SedanFactory(AbstractFactory):
    def create_bmw(self) -> BMW:
        return SedanBMW()

    def create_mercedes(self) -> Mercedes:
        return SedanMercedes()


class SuvFactory(AbstractFactory):
    def create_bmw(self) -> BMW:
        return SuvBMW()

    def create_mercedes(self) -> Mercedes:
        return SuvMercedes()


class BMW(ABC):
    @abstractmethod
    def confort_mode(self) -> str:
        pass


class SedanBMW(BMW):
    def confort_mode(self) -> str:
        return "Sedan BMW Confort Mode ON"


class SuvBMW(BMW):
    def confort_mode(self) -> str:
        return "SUV BMW Confort Mode ON"


class Mercedes(ABC):
    @abstractmethod
    def confort_mode(self) -> None:
        pass

    @abstractmethod
    def confort_mode_plus(self, collaborator: BMW) -> None:
        pass


class SedanMercedes(Mercedes):
    def confort_mode(self) -> str:
        return "Sedan Mercedes Mode ON"

    def confort_mode_plus(self, collaborator: BMW) -> str:
        result = collaborator.confort_mode()
        return f"Sedan Mercedes Confort+{result}"


class SuvMercedes(Mercedes):
    def confort_mode(self) -> str:
        return "SUV Mercedes Confort Mode ON"

    def confort_mode_plus(self, collaborator: BMW):
        result = collaborator.confort_mode()
        return f"SUV Mercedes Confort+{result}"


def client_code(factory: AbstractFactory) -> None:
    BMW = factory.create_bmw()
    Mercedes = factory.create_mercedes()

    print(f"{Mercedes.confort_mode()}")
    print(f"{Mercedes.confort_mode_plus(BMW)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(SedanFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(SuvFactory())
