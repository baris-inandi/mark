from src.lib.utils import minimal_indentation
from termcolor import cprint, colored

base_uri = "https://example.com"
docs_urls = {
    "require": "/require",
    "blocks": "/blocks",
    "selectors": "/selectors",
    "preprocess": "/styling/preprocessors",
    "module": "/modules"
}

err_file = "<unknown>"
err_line = 0


def error_file(x):
    global err_file
    err_file = x


def error_line(x):
    global err_line
    err_line = x


def complain(level: str, msg: str):
    complaints = {"INFO": "cyan", "WARN": "yellow", "ERROR": "red"}
    level = level.upper()
    if level not in complaints:
        return ""
    cprint(f"{level}: ", complaints[level], end="")
    print(msg)


def dump_lines(filename: str):
    print()
    try:
        line = err_line
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
    except Exception as e:
        cprint("Visualizer failed due to: ", "red", end="")
        print(e, end="\n\n")
        return


def throw(msg, no_exit: bool = False, **kwargs):
    print()
    if type(msg) == str:
        complain("error", msg)
    elif type(msg) == list:
        for m in msg:
            complain("error", m)

    dump_lines(err_file)

    cprint(f"[in {err_file}:{err_line}]", "blue")
    try:
        cprint(base_uri + docs_urls[kwargs["docs"]], attrs=["underline"])
    except KeyError:
        pass
    if not no_exit:
        print()
        exit(1)
