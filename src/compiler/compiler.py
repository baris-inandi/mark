from src.compiler.parser.parser import parse
from src.classes.dom import Dom
from src.compiler.utils.utils import set_wd
from src.compiler.parser.read_code_file import read_code_file
from os import getcwd, chdir
from os.path import isfile
from src.compiler.lang import minify
from src.compiler.lang.write_html import write_html
from src import config
from src.compiler.utils.error import throw
from termcolor import colored


def compile(f: str):
    if not isfile(f):
        f = colored(f, "yellow")
        throw(f'File not found: "{f}"')
    if not f.endswith(config.EXTENSION):
        f = colored(f, "yellow")
        throw(f'File must end with ".{config.EXTENSION}" extension: "{f}"')
    initial_cwd = getcwd()
    lines = read_code_file(f, False)
    set_wd(f)
    nodes = parse(lines, f)
    chdir(initial_cwd)
    dom = Dom(nodes)
    htmlout = dom.to_html()
    if config.MINIFY:
        htmlout = minify.html(htmlout)
    write_html(htmlout, f"{f[:len(config.EXTENSION)]}.html")
