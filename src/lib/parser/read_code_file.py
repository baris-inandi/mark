from src.lib.parser.remove_comments import remove_comments
from src.lib.error import throw
from termcolor import colored
from src import config


def read_code_file(filename: str, require_module: bool = False):
    try:
        with open(filename) as f:
            read_lines = f.readlines()
            if require_module and read_lines[0].strip(
            ) != config.module_decleration:
                mod_def = colored(config.module_decleration, "yellow")
                throw([
                    f"File not a module: \"{colored(filename, 'yellow')}\"",
                    f"Use \"{mod_def}\" in the first line of the file",
                    "to define a module."
                ],
                      docs="module")
            return remove_comments(read_lines).split("\n")
    except FileNotFoundError:
        s = colored(filename, "yellow")
        throw([
            f"File not found: {s}",
        ], docs="require")