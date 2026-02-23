
from lcddraw import center_str
from logger import Logger
from classes import *
from color import theme

font_h = 8
lines_on_screen = 240//font_h

class LogScreen(Screen):
    
    def __init__(self, manager):
        super().__init__(manager)
        self.scroll = 0

    def render(self, lcd):
        lcd.fill(theme().BG)

        total = len(Logger.lines)
        start = max(0, total - lines_on_screen - self.scroll)
        end = total - self.scroll
        
        y = 0
        for i in range(lines_on_screen):
            if i + self.scroll >= total: break
            line = Logger.lines[i+self.scroll]
            lcd.text(line[:27], 0, y, Logger.colors[i+self.scroll])
            y += font_h
    
    def update(self, input):
        if input.just_pressed("down"):
            self.down()
            self.dirty = True

        if input.just_pressed("up"):
            self.up()
            self.dirty = True
        if input.just_pressed("B"):
            self.result = ScreenResult.EXIT_APP    

            
    def down(self):
        if self.scroll < len(Logger.lines):
            self.scroll += 1

    def up(self):
        if self.scroll > 0:
            self.scroll -= 1