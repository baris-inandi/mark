from src.lib.parser.parser import parse
from src.classes.dom import Dom
from src.lib.utils import set_wd
from src.lib.parser.read_code_file import read_code_file
from os import getcwd, chdir


def run(f: str):
    initial_cwd = getcwd()
    lines = read_code_file(f, False)
    set_wd(f)
    nodes = parse(lines, f)
    chdir(initial_cwd)
    dom = Dom(nodes)
    htmlout = dom.to_html()
    print(htmlout)
