from src.lib.parser.parser import parse
from src.classes.dom import Dom
from src.lib.utils import set_wd
from os import getcwd, chdir


def run():
    # initial_cwd = getcwd()
    # set_wd("require-test/main.mark")
    nodes = parse("require-test/main.mark")
    # chdir(initial_cwd)
    dom = Dom(nodes)
    dom.to_html()
