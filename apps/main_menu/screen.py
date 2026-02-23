from classes import *
from lcddraw import center_str
from color import theme

class MainMenuScreen(Screen):    
    def __init__(self, app):
        super().__init__(app)
        self.items = app.manager.app_names
        self.apps = app.manager.all_apps
        self.index = 0
        self.scroll = 0

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
            self.result = ScreenResult.START_APP
            
        if input.just_pressed("Y"):
            raise Exception("Shutdown")
    
    def adjust_scroll(self):
        if self.index - self.scroll < 0:
            self.scroll = self.index
        if self.index - self.scroll > 4:
            self.scroll = self.index - 4

    def render(self, lcd):
        lcd.fill(theme().BG)
        
        center_str("PICOLATOR", 12, 4, theme().HEADING_SHADOW, lcd, offset=2)
        center_str("PICOLATOR", 10, 4, theme().HEADING_FG, lcd)
        
        
        for i in range(5):
            text = self.items[self.scroll + i]
            y = 50 + i * 35
            if i == self.index-self.scroll:
                lcd.fill_rect(20, y, 200, 35, theme().SELECTED_BG)
            center_str(text, y+6, 3, theme().TEXT_FG, lcd)

