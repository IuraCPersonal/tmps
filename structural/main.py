from adapter.Adapter import *
from facade.Facade import *

def main():
    socket  = Port()
    adapter = Adapter(socket)
    airpods  = Airpods(adapter)

    airpods.charge()

    choosen_theme = Theme('Welcome to iPhone')
    dark_theme = DarkTheme(choosen_theme)

    SetupiPhone().setup()

    return 0

if __name__ == "__main__":
    main()