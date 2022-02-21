from compiler.parser.parser import parse
from compiler.classes.dom import Dom
from utils.utils import set_wd
from compiler.parser.read_code_file import read_code_file
from os import getcwd, chdir
from os.path import isfile, basename
from compiler.lang import minify
from compiler.lang.write_html import write_html
from config import config
from utils.error import throw
from termcolor import colored, cprint

exist_checked = False


def compile(f: str, return_as_string=False, time_message=False):
    global exist_checked
    if not exist_checked:
        if not isfile(f):
            f = colored(f, "yellow")
            throw(f'File not found: "{f}"')
        if not f.endswith(config.EXTENSION):
            f = colored(f, "yellow")
            throw(f'File must end with ".{config.EXTENSION}" extension: "{f}"')
        exist_checked = True
    initial_cwd = getcwd()
    lines = read_code_file(f, False)
    set_wd(f)
    nodes = parse(lines, f)
    chdir(initial_cwd)
    dom = Dom(nodes)
    htmlout = dom.to_html()
    if config.MINIFY:
        htmlout = minify.html(htmlout)
    if return_as_string:
        return htmlout
    if time_message:
        cprint(f'[Compiled {f}]', "green")
    write_html(htmlout, f"{basename(f)[:len(config.EXTENSION)]}.html")
