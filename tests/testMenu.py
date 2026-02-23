from ui.screen import Screen

class MenuScreen(Screen):
    def __init__(self):
        super().__init__()
        self.items = ["Start", "Settings", "Info"]
        self.index = 0

    def update(self, input):
        if input.just_pressed("down"):
            self.index = (self.index + 1) % len(self.items)
            self.dirty = True

        if input.just_pressed("up"):
            self.index = (self.index - 1) % len(self.items)
            self.dirty = True

    def render(self, lcd):
        lcd.fill(lcd.white)
        for i, text in enumerate(self.items):
            y = 40 + i * 30
            if i == self.index:
                lcd.fill_rect(20, y, 200, 24, lcd.red)
            lcd.text(text, 30, y + 6, lcd.blue)
