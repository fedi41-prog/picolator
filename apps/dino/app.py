from classes import *

from apps.dino.screen import DinoRunnerScreen

class DinoRunnerApp(App):
    def on_start(self):
        self.screen = DinoRunnerScreen(self)

    def on_stop(self):
        pass