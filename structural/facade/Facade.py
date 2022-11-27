from decorator.Decorator import *

class TurnOn:
    def turn_on(self) -> str:
        print("Turning on...")


class ChooseLanguage:
    def choose_language(self) -> str:
        print("Choose your native language. Default: English...")


class ChooseTheme:
    def choose_theme(self, choice: int) -> str:
        welcome_msg = Theme('Welcome to iPhone')

        if choice:
            theme = DarkTheme(welcome_msg)
        else:
            theme = LightTheme(welcome_msg)
        
        print(theme.render())


# Facade
class SetupiPhone:
    def __init__(self):
        self.live = TurnOn()
        self.language = ChooseLanguage()
        self.theme = ChooseTheme()

    def setup(self):
        self.live.turn_on()
        self.language.choose_language()
        self.theme.choose_theme(1)