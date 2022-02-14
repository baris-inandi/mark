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
        out, parents_trace = "", [Node("_null", 0)]
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
                if node.indent < next_node.indent:
                    # parent
                    # right tab
                    out += " " * node.indent + node.opening_tag() + "\n"
                    parents_trace.append(node)
                elif node.indent > next_node.indent:
                    # child
                    # left tab
                    parent = parents_trace[-1]
                    out += " " * parent.indent + parent.closing_tag() + "\n"
                    parents_trace.pop()
                else:
                    # sibling
                    out += " " * node.indent + node.open_close_tag() + "\n"
        return out
