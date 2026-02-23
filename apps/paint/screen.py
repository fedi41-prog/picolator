from lcddraw import center_str
from logger import Logger
from classes import *
from color import to_color, Palette, theme

paint_colors = [
    0,
    0xffff,
    to_color(255, 0, 0),
    to_color(0, 255, 0),
    to_color(0, 0, 255),
]

size = 24
pixel_size = 10

class PaintScreen(Screen):
    
    def __init__(self, manager):
        super().__init__(manager)
        self.paint_idx = 0
        self.cursorX = size//2
        self.cursorY = size//2
        
        self.redraw_bg = True

    def render(self, lcd):
        if self.redraw_bg:
            lcd.fill(0xffff)
            self.redraw_bg = False
        
        lcd.fill_rect(
            self.cursorX*pixel_size,
            self.cursorY*pixel_size,
            pixel_size,
            pixel_size,
            paint_colors[self.paint_idx]
            )
    
    
    def update(self, input):
        if input.is_pressed("down"):
            self.cursorY += 1
            self.cursorY %= size
            self.dirty = True
        if input.is_pressed("up"):
            self.cursorY -= 1
            self.cursorY %= size
            self.dirty = True
        if input.is_pressed("left"):
            self.cursorX -= 1
            self.cursorX %= size
            self.dirty = True
        if input.is_pressed("right"):
            self.cursorX += 1
            self.cursorX %= size
            self.dirty = True
        
        if input.just_pressed("A"):
            self.paint_idx += 1
            self.paint_idx %= len(paint_colors)
        if input.just_pressed("B"):
            self.result = ScreenResult.EXIT_APP    