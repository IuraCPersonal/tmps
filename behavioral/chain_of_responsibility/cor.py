from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
import time

class Bootloader(ABC):
    @abstractmethod
    def set_next(self, handler: Bootloader) -> Bootloader:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractBootloader(Bootloader):
    _next_handler: Bootloader = None

    def set_next(self, handler: Bootloader) -> Bootloader:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class Drivers(AbstractBootloader):
    def handle(self, request: Any) -> str:
        if request == "NVIDIA":
            return f"Drivers: {request} started..."
        else:
            return super().handle(request)
    

class Taskbar(AbstractBootloader):
    def handle(self, request: Any) -> str:
        if request == "Pico":
            return f"Taskbar: {request} started..."
        else:
            return super().handle(request)


class WindowManager(AbstractBootloader):
    def handle(self, request: Any) -> str:
        if request == "xfce":
            return f"Window Manager: {request} started..."
        else:
            return super().handle(request)


class Client:
    @staticmethod
    def client_code(loader: Bootloader) -> None:

        for software in ['NVIDIA', 'Pico', 'xfce']:
            print(f'Trying to start {software}...')

            result = loader.handle(software)

            if result:
                print(f'[INFO] {result}')
            else:
                print(f'[INFO] Error, service could not start.')
            
            time.sleep(1)
            