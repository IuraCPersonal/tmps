class Theme:
    def __init__(self, theme: str) -> None:
        self._theme = theme

    def render(self) -> str:
        return self._theme


class LightTheme(Theme):
    def __init__(self, display: Theme) -> None:
        self._display = display

    def render(self) -> str:
        return f"{self._display.render()} - 🔥"


class DarkTheme(Theme):
    def __init__(self, display: Theme) -> None:
        self._display = display

    def render(self) -> str:
        return f"{self._display.render()} - 🌑"
