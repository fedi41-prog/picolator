from screens.MenuScreen import MenuScreen
from classes import *
from lcddraw import center_str
from theme import theme

class MainMenuScreen(MenuScreen):    
    def __init__(self, app):
        super().__init__(app)
        self.items = app.manager.app_names
        self.heading = "PICOLATOR"

    def update(self, input):
        super().update(input)
            
        if input.just_pressed("Y"):
            raise Exception("Shutdown")
    
    def on_click(self):
        self.result = ScreenResult.START_APP
    
