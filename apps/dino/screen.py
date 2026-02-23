from lcddraw import center_str, draw_pixels
from logger import Logger
from classes import *
from color import to_color, Palette, theme

import random

sprites = {}

sprites["dino"] = [(x, y) for x in range(5) for y in range(10)]

sprites["dino"].remove((3, 1))

sprites["dino"].remove((4, 4))
sprites["dino"].remove((3, 4))
sprites["dino"].remove((2, 4))
sprites["dino"].remove((1, 4))

sprites["cactus"] = [(1, y) for y in range(6)]
sprites["cactus"].append((0, 3))
sprites["cactus"].append((0, 4))
sprites["cactus"].append((2, 1))
sprites["cactus"].append((2, 2))


floor = 190
dino_height = 40
cactus_height = 24
jump_power = 18



def collide_rect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):

    # are the sides of one rectangle touching the other?

    return r1x + r1w >= r2x and r1x <= r2x + r2w and r1y + r1h >= r2y and r1y <= r2y + r2h  


class DinoRunnerScreen(Screen):
    
    def __init__(self, manager):
        super().__init__(manager)
        
        self.running = False
        self.dinoY = 0
        self.dinoYspeed = 0
        
        self.cactus_list = []
        
        self.ticks_before_new_cactus = 0
        
        self.speed = 5
        
        self.dinoX = 0

    def render(self, lcd):
        lcd.fill(to_color(170, 170, 255))
        
        lcd.fill_rect(0, floor, 240, 240-floor, to_color(150, 82, 32))

        draw_pixels(sprites["dino"], 40, floor-self.dinoY-dino_height, to_color(255, 255, 0), lcd, sz=4)
        
        for c in self.cactus_list:
            draw_pixels(sprites["cactus"], c, floor-cactus_height, to_color(0, 255, 0), lcd, sz=4)
        
        if not self.running:
            center_str("PRESS A", 100, 3, to_color(255, 0, 0), lcd)
            center_str("Dino runner:)", 50, 2, to_color(255, 255, 0), lcd)
    
    def update(self, input):
        if input.just_pressed("down"):
            self.dirty = True
        if input.just_pressed("up"):
            self.dirty = True
        if input.just_pressed("left"):
            self.dirty = True
        if input.just_pressed("right"):
            self.dirty = True
        
        if input.just_pressed("A"):
            self.running = not self.running
            self.dirty = True
        if input.just_pressed("B"):
            self.result = ScreenResult.EXIT_APP
        
        if self.running:
            if input.just_pressed("X"):
                self.jump()
                
            self.dinoY += self.dinoYspeed
            self.dinoYspeed -= 2
            
            if input.is_pressed("Y"):
                self.dinoYspeed -= 4
            
            if self.dinoY <= 0:
                self.dinoY = 0
                self.dinoYspeed = 0
            
            self.dinoX += 1
            self.speed = self.dinoX // 80 + 5
            
            new_list = []
            for c in self.cactus_list:
                if c > 0:
                    new_list.append(c-self.speed)
            self.cactus_list = new_list
            
            self.ticks_before_new_cactus -= 1
            if self.ticks_before_new_cactus <= 0:
                self.cactus_list.append(240)
                self.ticks_before_new_cactus = 20//self.speed + (random.randint(15, 20) * random.randint(0,2))
        
            self.dirty = True
            
    def jump(self):
        if self.dinoY == 0:
            self.dinoYspeed = jump_power
        