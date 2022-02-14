from src.classes.node import Node


class Dom:
    """
        class Dom:
        Represents a list of nodes that can be rendered to HTML.
    """
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes

    def to_html(self):
        out = ""
        for node in self.nodes:
            out += node.indent * " " + node.opening_tag() + "\n"
        return "<div></div>"
