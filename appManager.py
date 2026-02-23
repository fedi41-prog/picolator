from apps.main_menu.app import MainMenuApp
from apps.log.app import LogApp
from apps.calc.app import CalculatorApp
from apps.settings.app import SettingsApp
from apps.paint.app import PaintApp
from apps.dino.app import DinoRunnerApp

from classes import *
from logger import Logger

timeout = 10

class AppManager:
    def __init__(self, lcd):
        self.lcd = lcd
        self.current_app = None
        
        self.all_apps = [LogApp, CalculatorApp, SettingsApp, PaintApp, DinoRunnerApp, MainMenuApp, MainMenuApp, MainMenuApp]
        self.app_names = ["Log", "Calculator",  "Settings",  "Paint",  "Dino runner",  "App6",  "App7", "App8"]
        
        self.sleeping = False
        self.inactive_ticks = 0

    def start_app(self, app):
        if self.current_app:
            Logger.log("closing " + type(self.current_app).__name__, (0, 255, 0))
            self.current_app.on_stop()

        self.current_app = app
        
        Logger.log(type(app).__name__ + " starting!", (0, 255, 0))
        self.current_app.on_start()
        #self.lcd.fill(self.lcd.white)

    def update(self, input):
        if input.touching:
            self.inactive_ticks = 0
            if self.sleeping == True:
                Logger.log("sleep mode disabled", (255, 255, 0))
            self.sleeping = False
        else:
            self.inactive_ticks += 1
            if self.inactive_ticks % 100 == 0:
                Logger.log("inactive for: " + str(self.inactive_ticks) + " ticks")
            if self.inactive_ticks % 25 == 0:
                print("inactive for", self.inactive_ticks, "ticks")
            
        if self.inactive_ticks >= timeout*60:
            if self.sleeping == False:
                Logger.log("sleep mode enabled", (255, 255, 0))
            self.sleeping = True
        
        
        
        if not self.current_app or self.sleeping:
            self.lcd.fill(0)
            self.lcd.show()
            return
        
        

        self.current_app.update(input)


        r = self.current_app.consume_result()
        self.handle_result(r)

        self.current_app.render(self.lcd)
        self.lcd.show()
        
    def handle_result(self, result):
        if result == AppResult.EXIT:
            self.start_app(MainMenuApp(self))
        if result == AppResult.START_APP:
            self.start_app(self.current_app.next_app(self))

        
