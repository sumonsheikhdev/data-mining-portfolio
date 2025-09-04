import random
import yaml

with open("config/settings.yaml", "r") as f:
    settings = yaml.safe_load(f)
    print(settings)

def get_headers():
    return {"User-Agent": random.choice(settings["user_agents"])}
