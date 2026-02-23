
class Screen:
    def __init__(self, app):
        self.dirty = True  # muss neu gerendert werden?
        self.result = None
        self.app = app

    def on_enter(self):
        self.dirty = True

    def on_exit(self):
        pass

    def update(self, input):
        pass

    def render(self, lcd):
        pass
    
    
    def consume_result(self):
        r = self.result
        self.result = None
        return r

class InputState:
    def __init__(self, **buttons):
        self.buttons = buttons
        self.prev = {k: 1 for k in buttons}
        self.touching = False

    def update(self):
        self.pressed = {}
        self.touching = False
        for name, pin in self.buttons.items():
            v = pin.value()
            if v == 0: self.touching = True
            self.pressed[name] = (self.prev[name] == 1 and v == 0)
            self.prev[name] = v

    def down(self, name):
        return self.buttons[name].value() == 0

    def just_pressed(self, name):
        return self.pressed.get(name, False)
    
    def is_pressed(self, name):
        return not self.prev.get(name, True)


class App:
    def __init__(self, manager):
        self.screen = None
        self.result = AppResult.NONE
        self.manager = manager
        
        self.next_app = None

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def update(self, input):
        if self.screen:
            self.screen.update(input)
        r = self.screen.consume_result()
        self.handle_result(r)

    def render(self, lcd):
        if self.screen and self.screen.dirty:
            self.screen.render(lcd)
            self.screen.dirty = False
    def consume_result(self):
        r = self.result
        self.result = AppResult.NONE
        return r
    
    def handle_result(self, result):
        if result == ScreenResult.EXIT_APP:
            self.result = AppResult.EXIT


class AppResult:
    NONE = 0
    EXIT = 1
    START_APP = 2

class ScreenResult:
    NONE=0
    START_APP=1
    BACK=2
    EXIT_APP=3
    NEXT_SCREEN=4
    