from config import CONFIG, load_config

def to_color(R,G,B):
# Get RED value
    rp = int(R*31/255) # range 0 to 31
    if rp < 0: rp = 0
    r = rp *8
# Get Green value - more complicated!
    gp = int(G*63/255) # range 0 - 63
    if gp < 0: gp = 0
    g = 0
    if gp & 1:  g = g + 8192
    if gp & 2:  g = g + 16384
    if gp & 4:  g = g + 32768
    if gp & 8:  g = g + 1
    if gp & 16: g = g + 2
    if gp & 32: g = g + 4
# Get BLUE value       
    bp =int(B*31/255) # range 0 - 31
    if bp < 0: bp = 0
    b = bp *256
    colour = r+g+b
    return colour


    
    
class Palette:
    BLACK=0;
    WHITE=0xffff
    
    INK_BLACK=to_color(0, 8, 20)
    GOLD=to_color(255, 214, 10)
    
    DARK_GRAY=to_color(32, 32, 32)
    GRAY=to_color(51, 53, 51)
    LIGHT_GRAY=to_color(214, 214, 214)
    YELLOW=to_color(255, 238, 50)
    ORANGE=to_color(255, 209, 0)
    
    GREEN1=to_color(22, 219, 101)
    GREEN2=to_color(5, 140, 66)
    GREEN3=to_color(4, 71, 28)
    GREEN4=to_color(13, 40, 24)
    
    PURPLE=to_color(95, 15, 64)
    RED=to_color(154, 3, 30)
    PUMPKIN_YELLOW=to_color(251, 139, 36)
    DARK_ORANGE=to_color(227, 100, 20)
    TURQUISE=to_color(15, 76, 92)
    

class DarkTheme:
    BG=Palette.DARK_GRAY
    SELECTED_BG=Palette.GRAY
    
    HEADING_FG=Palette.ORANGE
    HEADING_SHADOW=Palette.YELLOW
    
    TEXT_FG=Palette.WHITE
    
class LightTheme:
    BG=Palette.WHITE
    SELECTED_BG=Palette.LIGHT_GRAY
    
    HEADING_FG=Palette.ORANGE
    HEADING_SHADOW= Palette.YELLOW
    
    TEXT_FG=Palette.BLACK
    
class HackerTheme:
    BG=Palette.BLACK
    SELECTED_BG=Palette.GREEN3
    
    HEADING_FG=Palette.GREEN2
    HEADING_SHADOW=Palette.GREEN1
    
    TEXT_FG=Palette.GREEN2
    
class HalloweenTheme:
    BG=Palette.TURQUISE
    SELECTED_BG=Palette.RED
    
    HEADING_FG=Palette.PUMPKIN_YELLOW
    HEADING_SHADOW=Palette.DARK_ORANGE
    
    TEXT_FG=Palette.PUMPKIN_YELLOW

    
all_themes = [DarkTheme(), LightTheme(), HackerTheme(), HalloweenTheme()]

load_config()

class CurrentTheme:
    th = all_themes[0]


def set_theme(th):
    CurrentTheme.th = th

def theme():
    return CurrentTheme.th
    


