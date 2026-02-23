from classes import *

from apps.paint.screen import PaintScreen

class PaintApp(App):
    def on_start(self):
        self.screen = PaintScreen(self)

    def on_stop(self):
        pass