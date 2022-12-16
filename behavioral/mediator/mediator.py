#!/usr/bin/env python3


from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class StartMenu(Mediator):
    def __init__(self, option_1: Shutdown, option_2: Sleep) -> None:
        self._option_1 = option_1
        self._option_1.mediator = self

        self._option_2 = option_2
        self._option_2.mediator = self


    def notify(self, sender: object, event: str) -> None:
        if event == 'Shutdown':
            print('System shutting down, please wait for:')
            self._option_1.write_log()
            self._option_1.close_apps()
        elif event == 'Sleep':
            print('System goes to sleep, please wait for:')
            self._option_1.write_log()


class BaseComponent:
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""

class Shutdown(BaseComponent):
    def write_log(self) -> None:
        print(' * Writing the Log file...')
        self.mediator.notify(self, 'Log')
    
    def close_apps(self) -> None:
        print(' * Closing Apps...')
        self.mediator.notify(self, 'Close')
    
    def shutdown(self) -> None:
        print('> Shutting down...')
        self.mediator.notify(self, 'Shutdown')


class Sleep(BaseComponent):
    def suspend(self, subject, service) -> None:
        print('> Suspneding...')
        # Disable the Update Service.
        subject.detach(service)
        self.mediator.notify(self, 'Sleep')