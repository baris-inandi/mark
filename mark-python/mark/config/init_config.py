from mark.config import config
import json
from os import getcwd, path


def init_config():
    if not path.exists("mark.config.json"):
        with open("mark.config.json", "w+") as f:
            f.write(json.dumps(config.user, indent=2) + "\n")
        print("Initialized Mark project at", getcwd())
    else:
        print("Already a Mark project")
