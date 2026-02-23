from classes import *
from lcddraw import center_str
from color import theme, all_themes, set_theme
from logger import Logger

class SettingsScreen(Screen):    
    def __init__(self, app):
        super().__init__(app)
        self.items = ["theme", "config1", "config2"]
        self.screens = [ThemeScreen(app), None, None]
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
            self.result = ScreenResult.NEXT_SCREEN
            
        if input.just_pressed("B"):
            self.result = ScreenResult.EXIT_APP
    
    def adjust_scroll(self):
        if self.index - self.scroll < 0:
            self.scroll = self.index
        if self.index - self.scroll > 4:
            self.scroll = self.index - 4

    def render(self, lcd):
        lcd.fill(theme().BG)
        
        center_str("Settings", 12, 4, theme().HEADING_SHADOW, lcd, offset=2)
        center_str("Settings", 10, 4, theme().HEADING_FG, lcd)
        
        
        for i in range(5):
            if self.scroll + i >= len(self.items): break
            text = self.items[self.scroll + i]
            y = 50 + i * 35
            if i == self.index-self.scroll:
                lcd.fill_rect(20, y, 200, 35, theme().SELECTED_BG)
            center_str(text, y+6, 3, theme().TEXT_FG, lcd)

class ThemeScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.index = 0

    def update(self, input):
        if input.just_pressed("right"):
            self.index = (self.index + 1) % len(all_themes)
            Logger.log("changing " + type(theme).__name__ + " theme to " + type(all_themes[self.index]).__name__, (0, 0, 255))
            set_theme(all_themes[self.index])
            self.dirty = True

        if input.just_pressed("left"):
            self.index = (self.index - 1) % len(all_themes)
            Logger.log("changing " + type(theme).__name__ + " theme to " + type(all_themes[self.index]).__name__, (0, 0, 255))
            set_theme(all_themes[self.index])
            self.dirty = True
            
        if input.just_pressed("B"):
            self.result = ScreenResult.BACK
    
    def render(self, lcd):
        lcd.fill(theme().BG)
        
        center_str("Theme", 12, 4, theme().HEADING_SHADOW, lcd, offset=2)
        center_str("Theme", 10, 4, theme().HEADING_FG, lcd)
        

        th = all_themes[self.index]
        center_str("theme: " + type(th).__name__, 60, 2, theme().TEXT_FG, lcd)
    