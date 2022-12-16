# BEHAVIORAL DESIGN PATTERNS IN PYTHON

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

# TABLE OF CONTENTS

1. CHAIN OF RESPONSIBILITY
2. MEDIATOR
3. MEMENTO
4. OBSERVER
5. STRATEGY
6. CONCLUSION

## CHAIN OF RESPONSIBILITY

`Chain of Responsibility` is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

### PROBLEM

Imagine that you’re working on an online ordering system. You want to restrict access to the system so only authenticated users can create orders. Also, users who have administrative permissions must have full access to all orders.

After a bit of planning, you realized that these checks must be performed sequentially. The application can attempt to authenticate a user to the system whenever it receives a request that contains the user’s credentials. However, if those credentials aren’t correct and authentication fails, there’s no reason to proceed with any other checks.

The code of the checks, which had already looked like a mess, became more and more bloated as you added each new feature. Changing one check sometimes affected the others. Worst of all, when you tried to reuse the checks to protect other components of the system, you had to duplicate some of the code since those components required some of the checks, but not all of them.

The system became very hard to comprehend and expensive to maintain. You struggled with the code for a while, until one day you decided to refactor the whole thing.

### SOLUTION

Like many other behavioral design patterns, the __Chain of Responsibility__ relies on transforming particular behaviors into stand-alone objects called handlers. In our case, each check should be extracted to its own class with a single method that performs the check. The request, along with its data, is passed to this method as an argument.

The pattern suggests that you link these handlers into a chain. Each linked handler has a field for storing a reference to the next handler in the chain. In addition to processing a request, handlers pass the request further along the chain. The request travels along the chain until all handlers have had a chance to process it.

Here’s the best part: a handler can decide not to pass the request further down the chain and effectively stop any further processing.

### EXAMPLE

In our example with `Operating System` here is how the patterns work.

```python
class Bootloader(ABC):
    @abstractmethod
    def set_next(self, handler: Bootloader) -> Bootloader:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass
```

We create a `Bootloader` to start all our Softwares/Drivers.

```python
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
```

Three main Software's implementation are the following:

```python
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
```

## MEDIATOR

Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

### PROBLEM

Say you have a dialog for creating and editing customer profiles. It consists of various form controls such as text fields, checkboxes, buttons, etc.

Some of the form elements may interact with others. For instance, selecting the “I have a dog” checkbox may reveal a hidden text field for entering the dog’s name. Another example is the submit button that has to validate values of all fields before saving the data.

By having this logic implemented directly inside the code of the form elements you make these elements’ classes much harder to reuse in other forms of the app. For example, you won’t be able to use that checkbox class inside another form, because it’s coupled to the dog’s text field. You can use either all the classes involved in rendering the profile form, or none at all.

### SOLUTION

The Mediator pattern suggests that you should cease all direct communication between the components which you want to make independent of each other. Instead, these components must collaborate indirectly, by calling a special mediator object that redirects the calls to appropriate components. As a result, the components depend only on a single mediator class instead of being coupled to dozens of their colleagues.

In our example with the profile editing form, the dialog class itself may act as the mediator. Most likely, the dialog class is already aware of all of its sub-elements, so you won’t even need to introduce new dependencies into this class.

### EXAMPLE

The Mediator interface declares a method used by components to notify the mediator about various events. The Mediator may react to these events and pass the execution to other components.

```python
class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass
```

Our system's `Start Menu` contains 2 main functions - to suspend the system and to shut it down.

```python
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
```

And here is how the options look like:

```python
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
```

## MEMENTO

Memento is a behavioral design pattern that lets you save and restore the previous state of an object without revealing the details of its implementation.

### PROBLEM

Imagine that you’re creating a text editor app. In addition to simple text editing, your editor can format text, insert inline images, etc.

At some point, you decided to let users undo any operations carried out on the text. This feature has become so common over the years that nowadays people expect every app to have it. For the implementation, you chose to take the direct approach. Before performing any operation, the app records the state of all objects and saves it in some storage. Later, when a user decides to revert an action, the app fetches the latest snapshot from the history and uses it to restore the state of all objects.

### SOLUTION

All problems that we’ve just experienced are caused by broken encapsulation. Some objects try to do more than they are supposed to. To collect the data required to perform some action, they invade the private space of other objects instead of letting these objects perform the actual action.

The Memento pattern delegates creating the state snapshots to the actual owner of that state, the originator object. Hence, instead of other objects trying to copy the editor’s state from the “outside,” the editor class itself can make the snapshot since it has full access to its own state.

The pattern suggests storing the copy of the object’s state in a special object called memento. The contents of the memento aren’t accessible to any other object except the one that produced it. Other objects must communicate with mementos using a limited interface which may allow fetching the snapshot’s metadata (creation time, the name of the performed operation, etc.), but not the original object’s state contained in the snapshot.

### EXAMPLE

For our System, `Memento` build our backup store - named _ShadowProtect_.

```python
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
```

And the caretaker (aka ShadowProtect):

```python
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
```

## OBSERVER

Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

### PROBLEM

Imagine that you have two types of objects: a Customer and a Store. The customer is very interested in a particular brand of product (say, it’s a new model of the iPhone) which should become available in the store very soon.

The customer could visit the store every day and check product availability. But while the product is still en route, most of these trips would be pointless.

### SOLUTION

The object that has some interesting state is often called subject, but since it’s also going to notify other objects about the changes to its state, we’ll call it publisher. All other objects that want to track changes to the publisher’s state are called subscribers.

The Observer pattern suggests that you add a subscription mechanism to the publisher class so individual objects can subscribe to or unsubscribe from a stream of events coming from that publisher. Fear not! Everything isn’t as complicated as it sounds. In reality, this mechanism consists of 1) an array field for storing a list of references to subscriber objects and 2) several public methods which allow adding subscribers to and removing them from that list.

### EXAMPLE

We all now that some services depend on eachother, therefore in my system - the responsability to start the System's services (`Time` and `Update`) are handled by the `Observer`.

```python
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
```

```python
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
```

And the implementation of the services and theirs responsabilities.

```python
class SystemUpdateService(Service):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("System Update Service: New Update Available.")


class SystemTimeService(Service):
    def update(self, subject: Subject) -> None:
        if subject._state >= 2 or subject._state == 0:
            print(f"System Time Service: {time.time()}. ⌚")
```

## STRATEGY

Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

### PROBLEM

One day you decided to create a navigation app for casual travelers. The app was centered around a beautiful map which helped users quickly orient themselves in any city.

One of the most requested features for the app was automatic route planning. A user should be able to enter an address and see the fastest route to that destination displayed on the map.

The first version of the app could only build the routes over roads. People who traveled by car were bursting with joy. But apparently, not everybody likes to drive on their vacation. So with the next update, you added an option to build walking routes. Right after that, you added another option to let people use public transport in their routes.

However, that was only the beginning. Later you planned to add route building for cyclists. And even later, another option for building routes through all of a city’s tourist attractions.

### SOLUTION

The Strategy pattern suggests that you take a class that does something specific in a lot of different ways and extract all of these algorithms into separate classes called strategies.

The original class, called context, must have a field for storing a reference to one of the strategies. The context delegates the work to a linked strategy object instead of executing it on its own.

The context isn’t responsible for selecting an appropriate algorithm for the job. Instead, the client passes the desired strategy to the context. In fact, the context doesn’t know much about strategies. It works with all strategies through the same generic interface, which only exposes a single method for triggering the algorithm encapsulated within the selected strategy.

This way the context becomes independent of concrete strategies, so you can add new algorithms or modify existing ones without changing the code of the context or other strategies.

### EXAMPLE

In my application the `Strategy` represents the `BIOS`, and more exactly - the `Boot Loader` aka _GRUB_.

```python
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
```

And just to represent it's purpose, here are a few `Operating Systems`.

```python
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
```

## CONCLUSION

During this laboratory work, I studied the `behavioral pattern` and implemented 5 of them in my current project which represents a Dummy Computer Simulator. The final result is as shown below:

```
GRUB: Press Enter to boot the selected OS.

Ubuntu 8.04, kernel Starting... Please wait

Trying to start NVIDIA...
[INFO] Drivers: NVIDIA started...
Trying to start Pico...
[INFO] Taskbar: Pico started...
Trying to start xfce...
[INFO] Window Manager: xfce started...

------------ System Started -------------

System: Starting service 🔆
System: Starting service 🔆

------------ Services Started -------------

System: I'm doing something important.
System: My state has just changed to: 4
System: Notifying services...
System Time Service: 1670868424.3762496. ⌚

System: I'm doing something important.
System: My state has just changed to: 0
System: Notifying services...
System Update Service: New Update Available.
System Time Service: 1670868424.3772495. ⌚

------------ Backup Time -------------

ShadowProtect: Saving Originator's state...
Backing Up 💾. Do not turn off your computer.
[BACKUP STATUS]: Last backup was successful. See oYfFNAQCxSuGdTnjOekXEsmaRgcbVK for more details.

> Suspneding...
System goes to sleep, please wait for:
 * Writing the Log file...
```