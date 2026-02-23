import json


CONFIG = {}

def load_config():
    global CONFIG
    
    with open("config.json", "r") as f:
        data = f.read()
        CONFIG = json.loads(data)
        
def dump_config():
    with open("config.json", "w") as f:
        f.write(json.dumps(data))
        