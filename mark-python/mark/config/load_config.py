from mark.utils.error import throw, complain
from mark.config import config
import json
from os import path


def load_config():
    for dir in range(10):
        config_file = ("../" * dir) + "mark.config.json"
        if path.exists(config_file):
            with open(config_file, "r") as f:
                loaded_config = json.load(f)
            print("found config file at", config_file)
            for k, v in loaded_config.items():
                if k in config.user:
                    config.user[k] = v
                else:
                    throw(f"Configuration key \"{k}\" is not defined.",
                          docs="config")
            break
    complain("warn", "No config file found. use `mark init` to create one.")
