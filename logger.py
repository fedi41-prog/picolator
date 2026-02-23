from color import to_color

class Logger:
    
    lines = []
    colors = []
    max_lines = 100

    def log(msg, color=(255, 255, 255)):
        #msg = " ".join(str(a) for a in args)
        
        Logger.colors.append(to_color(*color))
        Logger.lines.append(msg)
        if len(Logger.lines) > Logger.max_lines:
            Logger.lines.pop(0)
            Logger.colors.pop(0)
        file=open('log.txt', 'a')
        file.write(msg + "\n")
        file.flush()
        file.close()
