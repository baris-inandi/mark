from src.lib.parser.remove_comments import remove_comments
from src.lib.error import throw
from termcolor import colored
from src import config
from os import getcwd


def read_code_file(filename: str, require_module: bool = False):
    # TODO: does not work at all, for some reason :/
    try:
        with open(filename) as f:
            read_lines = f.readlines()
            if require_module and read_lines[0].strip(
            ) != config.MODULE_DECLERATION:
                mod_def = colored(config.MODULE_DECLERATION, "yellow")
                throw([
                    f"File not a module: \"{colored(filename, 'yellow')}\"",
                    f"Use \"{mod_def}\" in the first line of the file",
                    "to define a module."
                ],
                      docs="module")
            return remove_comments(read_lines).split("\n")
    except FileNotFoundError:
        s = colored(filename, "yellow")
        throw([f"File not found: {s}", f"in working directory: {getcwd()}"],
              docs="require")
