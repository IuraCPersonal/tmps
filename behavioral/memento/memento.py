from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits


class Backup():
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        

    def work(self) -> None:
        """
        The System's logic may affect its internal state.
        Therefore, the client should backup the state before launching methods
        of the business logic via the save() method.
        """

        print("Backing Up 💾. Do not turn off your computer.")
        self._state = self._generate_random_string(30)
        print(f"[BACKUP STATUS]: Last backup was successful. See {self._state} for more details.")


    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))


    def save(self) -> Memento:
        return ConcreteMemento(self._state)


    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"[BACKUP STATUS]: Restoring data from {self._state}.")


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]


    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date
    

class ShadowProtect():
    def __init__(self, originator: Backup) -> None:
        self._mementos = []
        self._originator = originator


    def backup(self) -> None:
        print("\nShadowProtect: Saving Originator's state...")
        self._mementos.append(self._originator.save())


    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()

        print(f"ShadowProtect: Restoring state to: {memento.get_name()}")

        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("ShadowProtect: Here's the list of backups:")

        for memento in self._mementos:
            print(memento.get_name())