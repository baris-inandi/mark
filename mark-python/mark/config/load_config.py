from mark.utils.error import throw
from mark.config import config
import json
from os import path


def load_config():
    if path.exists("mark.config.json"):
        with open("mark.config.json", "r") as f:
            loaded_config = json.load(f)
        for k, v in loaded_config.items():
            if k in config.user:
                config.user[k] = v
            else:
                throw(f"Config key '{k}' is not defined.")
    else:
        throw([
            "mark.config.json not found.",
            "run 'mark init' to initialize a Mark project"
        ])
