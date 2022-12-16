from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List
import time


class Subject(ABC):
    @abstractmethod
    def attach(self, service: Service) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, service: Service) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ServiceManager(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    _services: List[Service] = []

    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    def attach(self, service: Service) -> None:
        print("System: Starting service 🔆")
        self._services.append(service)

    def detach(self, service: Service) -> None:
        self._services.remove(service)

    
    def notify(self) -> None:
        print("System: Notifying services...")
        for service in self._services:
            service.update(self)
    
    def work(self) -> None:
        print("\nSystem: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"System: My state has just changed to: {self._state}")
        self.notify()


class Service(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


class SystemUpdateService(Service):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("System Update Service: New Update Available.")


class SystemTimeService(Service):
    def update(self, subject: Subject) -> None:
        if subject._state >= 2 or subject._state == 0:
            print(f"System Time Service: {time.time()}. ⌚")