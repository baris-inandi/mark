from mark.config import config
import json
from os import getcwd, path


def init_config():
    if not path.exists("markrc.json"):
        with open("markrc.json", "w+") as f:
            f.write(json.dumps(config.user, indent=2) + "\n")
        print("Initialized Mark project at", getcwd())
    else:
        print("Already a Mark project")
