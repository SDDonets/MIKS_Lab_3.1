from skin import Skin


class WinampSkin(Skin):
    """A specific implementation of a skin in the style of Winamp"""

    def draw_window_frame(self, window):
        print("We draw a FRAME in Winamp style")

    def draw_window_titlebar(self, window):
        print("We draw the HEADER in Winamp style")

    def draw_window_buttons(self, window):
        print("We draw BUTTONS in Winamp style")

    def draw_window_background(self, window):
        print("We draw a background in Winamp style")