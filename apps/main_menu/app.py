from classes import *
from apps.main_menu.screen import MainMenuScreen

class MainMenuApp(App):
    def on_start(self):
        self.screen = MainMenuScreen(self)

    def on_stop(self):
        pass
    
    def handle_result(self, result):
        if result == ScreenResult.START_APP:
            self.result = AppResult.START_APP
            self.next_app = self.screen.apps[self.screen.index]


    
    