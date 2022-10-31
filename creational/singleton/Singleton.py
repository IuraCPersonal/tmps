class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def dummy_funct(self) -> None:
        pass


if __name__ == '__main__':

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s1):
        print('Singleton Works, both variables contain the same instance.')
    else:
        print('Fail...')