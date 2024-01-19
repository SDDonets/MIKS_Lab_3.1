from skin import Skin


class RetroSkin(Skin):
    """A specific implementation of the retro-style skin"""

    def draw_window_frame(self, window):
        print("We draw a FRAME in retro style")

    def draw_window_titlebar(self, window):
        print("We draw the TITLE in a retro style")

    def draw_window_buttons(self, window):
        print("We draw BUTTONS in retro style")

    def draw_window_background(self, window):
        print("We draw the BACKGROUND in a retro style")