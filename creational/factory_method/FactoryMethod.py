from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def create_car(self):
        pass

    def start_car(self) -> str:
        car = self.create_car()

        result = f'Creator: {car.operation()} was created'

        return result


class BMWCreator(Creator):
    def create_car(self) -> Car:
        return BMW()


class MercedesCreator(Creator):
    def create_car(self) -> Car:
        return Mercedes()


class Car(ABC):
    def operation(self) -> str:
        pass


class BMW(Car):
    def operation(self) -> str:
        return "{This is a BMW}"


class Mercedes(Car):
    def operation(self) -> str:
        return "{This is a Mercedes}"


def client_code(creator: Creator) -> None:
    print(f"Client: {creator.start_car()}", end="")


if __name__ == '__main__':
    print("App: BMW Factory Starts...")
    client_code(BMWCreator())

    print("\n")

    print("App: Mercedes Factory Starts...")
    client_code(MercedesCreator())