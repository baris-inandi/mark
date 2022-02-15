from src.classes.node import Node


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
                # if node.tag == "_plaintext":
                #    continue
                # elif node.tag == "_document":
                #    continue
                # TODO: use the above to handle
                # document insertion
                # and html plaintext
                next_node = self.nodes[index + 1]
                node.parse_attr()
                out += " " * node.indent + node.opening_tag() + "\n"
                if node.indent < next_node.indent:
                    # right tab
                    stack.append(node)
                else:
                    # left tab
                    if node.indent > next_node.indent:
                        stack.pop()
                    parent = stack[-1]
                    out += " " * parent.indent + parent.closing_tag() + "\n"
        return out
