from mediator.mediator import *


if __name__ == '__main__':
    # Do something


    suspend = Sleep()
    shutdown = Shutdown()

    mediator = StartMenu(shutdown, suspend)

    # User triggers the Sleep Option.
    suspend.suspend()

    # User triggers the Shutdown Option.
    # shutdown.shutdown()