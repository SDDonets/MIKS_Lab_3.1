from abc import ABC, abstractmethod


class Skin(ABC):
    """
    Abstract base class for skins.
    Defines mandatory methods that specific skins must implement.
    """

    @abstractmethod
    def draw_window_frame(self, window):
        pass

    @abstractmethod
    def draw_window_titlebar(self, window):
        pass

    @abstractmethod
    def draw_window_buttons(self, window):
        pass

    @abstractmethod
    def draw_window_background(self, window):
        pass