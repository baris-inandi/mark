from src.lib.parser.parser import parse
from src.classes.dom import Dom
from src.lib.utils import set_wd
from src.lib.parser.read_code_file import read_code_file
from os import getcwd, chdir


def run():
    initial_cwd = getcwd()
    lines = read_code_file("require-test/main.mark", False)
    set_wd("require-test/main.mark")
    nodes = parse(lines, "require-test/main.mark")
    chdir(initial_cwd)
    dom = Dom(nodes)
    dom.to_html()
