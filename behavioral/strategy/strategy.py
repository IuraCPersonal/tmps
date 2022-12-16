from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BIOS():
    def __init__(self, os: OS) -> None:
        self._os = os


    @property
    def os(self) -> OS:
        return self._os


    @os.setter
    def os(self, os: OS) -> None:
        self._os = os


    def boot_loader(self) -> None:
        print("GRUB: Press Enter to boot the selected OS.")
        input()
        result = self._os.boot()
        print(f'{result} Starting... Please wait')


class OS(ABC):
    @abstractmethod
    def boot(self, data: str):
        pass


class Ubuntu(OS):
    def boot(self) -> str:
        return 'Ubuntu 8.04, kernel'


class Arch(OS):
    def boot(self) -> str:
        return 'ArchLinux 16.0'