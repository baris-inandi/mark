from src.lib.parser.parser import parse
from src.classes.dom import Dom


def run():
    nodes = parse("idea")
    dom = Dom(nodes)
    dom.to_html()
