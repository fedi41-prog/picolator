from classes import *

from apps.calc.screen import CalculatorScreen

class CalculatorApp(App):
    def on_start(self):
        self.screen = CalculatorScreen(self)

    def on_stop(self):
        pass