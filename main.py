from LCD13 import LCD_1inch3 
from machine import Pin, SPI, PWM
import time
from classes import *
from appManager import AppManager
from apps.main_menu.app import MainMenuApp
from apps.log.app import LogApp
from logger import Logger
from config import load_config, CONFIG

import gc

import os



BL = 13 # Backlight


led = Pin(25, Pin.OUT)

#print("starting signal...")
#for i in range(5):
#    led.high()
#    time.sleep(0.07)
#    led.low()

#    time.sleep(0.07)
#print("executing!")
Logger.log("===================", (255, 0, 255))
Logger.log("picolator starting!", (255, 0, 255))
Logger.log("===================", (255, 0, 255))

load_config()

Logger.log(str(CONFIG), (255, 255, 255))

pwm = PWM(Pin(BL))
default_duty = 40000

print(1000/60 )

def main():
    
    pwm.freq(1000)
    pwm.duty_u16(default_duty)


    lcd = LCD_1inch3()
    
    input = InputState(
        up=Pin(2, Pin.IN, Pin.PULL_UP),
        down=Pin(18, Pin.IN, Pin.PULL_UP),
        left=Pin(16, Pin.IN, Pin.PULL_UP),
        right=Pin(20, Pin.IN, Pin.PULL_UP),
        A=Pin(15, Pin.IN, Pin.PULL_UP),
        B=Pin(17, Pin.IN, Pin.PULL_UP),
        X=Pin(19, Pin.IN,Pin.PULL_UP),
        Y=Pin(21, Pin.IN,Pin.PULL_UP)
    )
    
  
    manager = AppManager(lcd)
    manager.start_app(MainMenuApp(manager))
    
    sleeping = False
    
    while True:
        input.update()
        manager.update(input)
        if manager.sleeping and not sleeping:
            pwm.freq(0)
            pwm.duty_u16(0)
            sleeping = True
        if sleeping and not manager.sleeping:
            pwm.freq(1000)
            pwm.duty_u16(default_duty)
            sleeping = False
        
        
        time.sleep_ms(7) 

try:
    main()
except Exception as e:
    print(e)
    Logger.log("Exception: " + str(e))
    with open("crash.txt", "a") as f:
        f.write(str(e))
finally: 
    pwm.freq(0)
    pwm.duty_u16(0)

    time.sleep(0.5)
    
    for i in range(5):
        led.high()
        time.sleep(0.07)
        led.low()
        time.sleep(0.07)
    

    
    