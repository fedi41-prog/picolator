
from lcddraw import center_str
from logger import Logger
from classes import *
from theme import theme

class CalculatorScreen(Screen):
    
    def __init__(self, manager):
        super().__init__(manager)

    def render(self, lcd):
        lcd.fill(theme().SURFACE)

        lcd.fill_rect(10, 10, 220, 30, theme().PRIMARY)
    
    def update(self, input):
        if input.just_pressed("down"):
            self.dirty = True
        if input.just_pressed("up"):
            self.dirty = True
        if input.just_pressed("left"):
            self.dirty = True
        if input.just_pressed("right"):
            self.dirty = True
        
        if input.just_pressed("A"):
            pass
        if input.just_pressed("B"):
            self.result = ScreenResult.EXIT_APP    