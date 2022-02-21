from compiler.classes.node import Node


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
                    parent = stack[-1]
                    stack.pop()
                    out += parent.closing_tag()
        stack.reverse()
        for close_node in stack:
            out += close_node.closing_tag()
        return out
