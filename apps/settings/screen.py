from classes import *
from lcddraw import center_str
from theme import theme, all_themes, update_theme_from_config
from logger import Logger
from config import CONFIG, dump_config
from screens.MenuScreen import MenuScreen

class SettingsScreen(MenuScreen):    
    def __init__(self, app):
        super().__init__(app)
        self.items = ["theme", "config1", "config2"]
        self.screens = [ThemeScreen(app), None, None]
        self.heading = "Settings"


    def on_click(self):
        self.result = ScreenResult.NEXT_SCREEN
            
                

class ThemeScreen(Screen):
    def __init__(self, app):
        super().__init__(app)
        self.index = 0

    def update(self, input):
        if input.just_pressed("right"):
            self.index = (self.index + 1) % len(all_themes)
            Logger.log("changing " + type(theme).__name__ + " theme to " + type(all_themes[self.index]).__name__, (0, 0, 255))
            
            CONFIG()["theme"] = self.index
            update_theme_from_config()
            
            self.dirty = True

        if input.just_pressed("left"):
            self.index = (self.index - 1) % len(all_themes)
            Logger.log("changing " + type(theme).__name__ + " theme to " + type(all_themes[self.index]).__name__, (0, 0, 255))
            
            CONFIG()["theme"] = self.index
            update_theme_from_config()
            
            self.dirty = True
            
        if input.just_pressed("B"):
            self.result = ScreenResult.BACK
            dump_config()
            
    
    def render(self, lcd):
        lcd.fill(theme().SURFACE)
        
        center_str("Theme", 12, 4, theme().PRIMARY_CONTAINER, lcd, offset=2)
        center_str("Theme", 10, 4, theme().PRIMARY, lcd)
        

        th = all_themes[self.index]
        center_str("theme: " + type(th).__name__, 60, 2, theme().SECONDARY, lcd)
    