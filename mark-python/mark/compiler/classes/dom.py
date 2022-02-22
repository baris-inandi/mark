from mark.compiler.classes.node import Node
from mark.utils.error import throw
from mark.config import config


class Dom:
    """
        class Dom:
        Represents a list of nodes that can be transpiled to HTML.
    """
    def __init__(self, nodes: list[Node]):
        self.nodes = [
            Node("_null", 0),
            *nodes,
            Node("_null", 0),
        ]

    def to_html(self):
        out, stack = "", [Node("_null", 0)]
        for index, node in enumerate(self.nodes):
            if node.tag != "_null":
                next_node = self.nodes[index + 1]
                node.parse_attr()
                out += node.opening_tag()
                if node.indent >= next_node.indent:
                    out += node.closing_tag()
                if node.indent < next_node.indent:
                    stack.append(node)
                elif node.indent > next_node.indent:
                    try:
                        indent_difference = node.indent - next_node.indent
                        if indent_difference % config.user["indent"] != 0:
                            throw("Indentation error")
                        indent_difference //= config.user["indent"]
                        for _ in range(indent_difference):
                            parent = stack[-1]
                            stack.pop()
                            out += parent.closing_tag()
                    except Exception:
                        throw("Indentation error")
        stack.reverse()
        for close_node in stack:
            out += close_node.closing_tag()
        return out
