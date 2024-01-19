from main_window import MainWindow
from settings_window import SettingsWindow
from winamp_skin import WinampSkin
from retro_skin import RetroSkin


# We create window objects
main_window = MainWindow(WinampSkin())
settings_window = SettingsWindow(RetroSkin())

# We display windows with skins
main_window.draw()
settings_window.draw()

# We demonstrate the change of skin in runtime
main_window.skin = RetroSkin()
main_window.draw()