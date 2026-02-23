from classes import *

from apps.log.screen import LogScreen

class LogApp(App):
    def on_start(self):
        self.screen = LogScreen(self)

    def on_stop(self):
        pass