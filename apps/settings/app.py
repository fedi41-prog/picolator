from classes import *

from apps.settings.screen import SettingsScreen

class SettingsApp(App):
    def on_start(self):
        self.screen = SettingsScreen(self)

    def on_stop(self):
        pass
    
    def handle_result(self, result):
        super().handle_result(result)
        if result == ScreenResult.NEXT_SCREEN and type(self.screen) == SettingsScreen:
            self.screen = self.screen.screens[self.screen.index]
        if result == ScreenResult.BACK:
            self.screen = SettingsScreen(self)