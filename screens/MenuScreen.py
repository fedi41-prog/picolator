from theme import theme
from classes import *
from lcddraw import *

class MenuScreen(Screen):    
    def __init__(self, app):
        super().__init__(app)
        self.items = []
        self.index = 0
        self.scroll = 0
        self.heading = "<< MENU >>"

    def update(self, input):
        if input.just_pressed("down"):
            self.index = (self.index + 1) % len(self.items)
            self.adjust_scroll()
            self.dirty = True

        if input.just_pressed("up"):
            self.index = (self.index - 1) % len(self.items)
            self.adjust_scroll()
            self.dirty = True
            
        if input.just_pressed("A"):
            self.on_click()
            
        if input.just_pressed("B"):
            self.result = ScreenResult.EXIT_APP
        
    def on_click(self):
        pass
    
    def adjust_scroll(self):
        if self.index - self.scroll < 0:
            self.scroll = self.index
        if self.index - self.scroll > 4:
            self.scroll = self.index - 4

    def render(self, lcd):
        lcd.fill(theme().SURFACE)
        
        lcd.fill_rect(0, 0, 240, 50, theme().PRIMARY_CONTAINER)
        
        center_str(self.heading, 12, 4, theme().PRIMARY, lcd, offset=2)
        center_str(self.heading, 10, 4, theme().ON_PRIMARY, lcd)
        
        
        for i in range(min(5, len(self.items))):
            text = self.items[self.scroll + i]
            y = 60 + i * 35
            if i == self.index-self.scroll:
                lcd.fill_rect(20, y, 200, 35, theme().SECONDARY)
                center_str(text, y+6, 3, theme().ON_SECONDARY, lcd)
            else:
                center_str(text, y+6, 3, theme().SECONDARY, lcd)