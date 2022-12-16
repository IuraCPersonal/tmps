from mediator.mediator import *
from observer.observer import *
from chain_of_responsibility.cor import *
from memento.memento import *
from strategy.strategy import *

if __name__ == '__main__':
    operating_system = BIOS(Ubuntu())
    operating_system.boot_loader()

    time.sleep(2)

    nvidia = Drivers()
    taskbar = Taskbar()
    wm = WindowManager()

    backup = Backup('The Quick Brown Fox')
    shadow_protect = ShadowProtect(backup)

    nvidia.set_next(wm).set_next(taskbar)

    Client.client_code(nvidia)

    time.sleep(2)
    
    print('------------ System Started -------------')

    subject = ServiceManager()

    update_service = SystemUpdateService()
    subject.attach(update_service)

    time_service = SystemTimeService()
    subject.attach(time_service)

    time.sleep(2)

    print('------------ Services Started -------------')


    subject.work()
    subject.work()

    suspend = Sleep()
    shutdown = Shutdown()

    mediator = StartMenu(shutdown, suspend)

    time.sleep(2)

    print('------------ Backup Time -------------')
    
    shadow_protect.backup()
    backup.work()

    time.sleep(1)

    # User triggers the Sleep Option.
    suspend.suspend(subject, update_service)

    # User triggers the Shutdown Option.
    # shutdown.shutdown()