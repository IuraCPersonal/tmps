from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    @property
    @abstractmethod
    def car(self) -> None:
        pass

    @abstractmethod
    def produce_wheels() -> None:
        pass

    @abstractmethod
    def produce_brakes(self) -> None:
        pass

    @abstractmethod
    def produce_engine(self) -> None:
        pass

class BMWBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._car = BMW()

    @property
    def car(self) -> BMW:
        car = self._car
        self.reset()
        return car

    def produce_wheels(self) -> None:
        self._car.add("Wheels")

    def produce_brakes(self) -> None:
        self._car.add("Brakes")

    def produce_engine(self) -> None:
        self._car.add("Engine")

class BMW():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Car parts: {', '.join(self.parts)}", end="")

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_car(self) -> None:
        self.builder.produce_engine()

    def build_full_car(self) -> None:
        self.builder.produce_engine()
        self.builder.produce_wheels()
        self.builder.produce_brakes()

if __name__ == '__main__':
    director = Director()
    builder = BMWBuilder()
    director.builder = builder

    print('Standard Basic Car')
    director.build_minimal_car()
    builder.car.list_parts()

    print("\n")

    print('Standard Full Car')
    director.build_full_car()
    builder.car.list_parts()
