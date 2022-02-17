from src.utils.utils import minimal_indentation
from termcolor import cprint, colored
from src import config

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
    try:
        out = ""
        line = err_line
        with open(filename) as f:
            lines = f.readlines()
        lines = [*([""] * 3), *lines, *([""] * 3)]
        lines = minimal_indentation(lines[line:line + 5])
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
            out += (f"{lhs}  {truncated_code}")
        print("\n", out)
    except Exception:
        return


def throw(msg, **kwargs):
    if type(msg) == str:
        complain("error", msg)
    elif type(msg) == list:
        for m in msg:
            complain("error", m)

    dump_lines(err_file)

    print(f"[in {err_file}:{err_line}]")
    try:
        cprint(base_uri + docs_urls[kwargs["docs"]], attrs=["underline"])
    except KeyError:
        pass
    if not config.ERROR_NO_EXIT:
        exit(1)
    else:
        raise Exception(msg)
