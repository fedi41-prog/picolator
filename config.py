import json



class Config:
    config = {}

def CONFIG():
    return Config.config



def load_config():
    
    
    with open("config.json", "r") as f:
        data = f.read()
        Config.config = json.loads(data)

        
def dump_config():
    with open("config.json", "w") as f:
        f.write(json.dumps(Config.config))