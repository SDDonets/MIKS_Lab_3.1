from windows import Window


class MainWindow(Window):
    """A specific implementation of the main program window"""

    def __init__(self, skin):
        super().__init__(skin)

    def draw(self):
        print("We draw the main window")
        super().draw()

    def handle_mouse_click(self, x, y):
        print("We process a mouse click in the main window")
        # there is some logic here