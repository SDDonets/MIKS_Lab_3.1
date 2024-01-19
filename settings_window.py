from windows import Window


class SettingsWindow(Window):
    """The settings window class"""

    def __init__(self, skin):
        super().__init__(skin)

    def draw(self):
        print("We draw the Settings window")
        super().draw()

    def handle_mouse_click(self, x, y):
        print("Mouse event handling in the Settings window")
        # here is the processing logic