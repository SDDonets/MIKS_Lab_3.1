from abc import ABC, abstractmethod


class Window(ABC):
    """
    Abstract base class for windows.
    Defines mandatory methods that specific windows must implement.
    """

    def __init__(self, skin):
        self.skin = skin

    @abstractmethod
    def draw(self):
        self.skin.draw_window_frame(self)
        self.skin.draw_window_titlebar(self)
        self.skin.draw_window_buttons(self)
        self.skin.draw_window_background(self)

    @abstractmethod
    def handle_mouse_click(self, x, y):
        pass