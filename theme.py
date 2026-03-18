from config import CONFIG
from color import hex_color

class BasicTheme:
    SURFACE=0
    ON_SURFACE=0xffff
    
    PRIMARY=0xffff
    ON_PRIMARY=0
    PRIMARY_CONTAINER=0
    ON_PRIMARY_CONTAINER=0xffff
    
    SECONDARY=0xffff
    ON_SECONDARY=0
    SECONDARY_CONTAINER=0
    ON_SECONDARY_CONTAINER=0xffff
    

class DarkTheme(BasicTheme):
    SURFACE=0
    ON_SURFACE=0xffff
    
    PRIMARY=0xffff
    ON_PRIMARY=0
    PRIMARY_CONTAINER=0
    ON_PRIMARY_CONTAINER=0xffff
    
    SECONDARY=0xffff
    ON_SECONDARY=0
    SECONDARY_CONTAINER=0
    ON_SECONDARY_CONTAINER=0xffff
    
class GreenTheme(BasicTheme):
    SURFACE=hex_color("#263238")
    ON_SURFACE=hex_color("#ECEFF1")
    
    PRIMARY=hex_color("#558B2F")
    ON_PRIMARY=hex_color("#F1F8E9")
    PRIMARY_CONTAINER=hex_color("#8BC34A")
    ON_PRIMARY_CONTAINER=hex_color("#DCEDC8")
    
    SECONDARY=hex_color("#D84315")
    ON_SECONDARY=hex_color("#FFF3E0")
    SECONDARY_CONTAINER=hex_color("#F57C00")
    ON_SECONDARY_CONTAINER=hex_color("#FFE0B2")

class GrayscaleTheme(BasicTheme):
    SURFACE=hex_color("#212121")
    ON_SURFACE=hex_color("#FAFAFA")
    
    PRIMARY=hex_color("#424242")
    ON_PRIMARY=hex_color("#F5F5F5")
    PRIMARY_CONTAINER=hex_color("#BDBDBD")
    ON_PRIMARY_CONTAINER=hex_color("#212121")
    
    SECONDARY=hex_color("#BDBDBD")
    ON_SECONDARY=hex_color("#424242")
    SECONDARY_CONTAINER=hex_color("#9E9E9E")
    ON_SECONDARY_CONTAINER=hex_color("#424242")


    
# ===================

all_themes = [DarkTheme(), GreenTheme(), GrayscaleTheme()]

class CurrentTheme:
    th = all_themes[0]

def update_theme_from_config():
    print(CONFIG())
    set_theme_id(CONFIG()["theme"])

def set_theme_id(i):
    set_theme(all_themes[i])

def set_theme(th):
    CurrentTheme.th = th

def theme():
    return CurrentTheme.th
    


