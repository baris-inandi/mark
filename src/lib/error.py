from src.lib.utils import minimal_indentation
from termcolor import cprint, colored

base_uri = "https://example.com"
docs_urls = {
    "require": "/require",
    "blocks": "/blocks",
    "selectors": "/selectors",
    "preprocess": "/styling/preprocessors"
}

file = "<unknown>"


def error_file(f):
    global file
    file = f


def complain(level: str, msg: str):
    complaints = {"INFO": "cyan", "WARN": "yellow", "ERROR": "red"}
    level = level.upper()
    if level not in complaints:
        return ""
    cprint(f"{level}: ", complaints[level], end="")
    print(msg)


def dump_lines(filename: str, line: int):
    line = 20
    try:
        line -= 1
        print()
        with open(filename) as f:
            lines = f.readlines()
        lines = [*([""] * 3), *lines, *([""] * 3)]
        lines = minimal_indentation(lines[line + 1:line + 6])
        for i, current in enumerate(lines):
            if current == "":
                current = "\n"
            j = line + i - 2
            causes_err = j == line
            gutter = " > " if causes_err else "   "
            gutter_seperator = "┃" if causes_err else "│"
            truncated_code = (current[:40] + (current[40:] and '...\n'))

            lhs = f"{gutter}{j + 1} {gutter_seperator}"
            if causes_err:
                lhs = colored(lhs, "white", "on_red")
            print(f"{lhs}  {truncated_code}", end="")
        print()
    except Exception:
        return


def throw(msg, no_exit: bool = False, **kwargs):
    print()
    if type(msg) == str:
        complain("error", msg)
    elif type(msg) == list:
        for m in msg:
            complain("error", m)

    line = kwargs.get("line", "<unknown>")
    dump_lines(file, line)
    cprint(f"[in {file}:{line}]", "blue")
    try:
        cprint(base_uri + docs_urls[kwargs["docs"]], attrs=["underline"])
    except KeyError:
        pass
    if not no_exit:
        print()
        exit(1)
