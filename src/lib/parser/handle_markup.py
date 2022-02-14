from src.lib.require.require import require
from src.classes.node import Node
from src.lib.utils import indentation_level


def handle_markup(tree: list[Node], line: str, index: int) -> list[Node]:
    """
        Determines type of line
        Possible Cases:
            - extension statement (and .foo)
            - plaintext element ("foo")
            - node (<div />)
    """
    code = line.strip()
    split_code = code.split(" ", 1)
    tag = split_code[0]
    props = split_code[-1]
    if tag == "and":
        # Extension statement
        # appends extension props to <Node>.code
        tree[-1].code += f' {props}'
    elif code[0] in ["'", '"'] and code[-1] in ["'", '"']:
        # Plaintext
        n = Node("_plaintext", index + 1)
        n.block_inner = code[1:-1]
        n.indent = indentation_level(line)
        tree.append(n)
    elif tag == "require":
        # Require statement
        tree.append(require(line, index + 1))
    else:
        # Node
        tree.append(Node(line, index + 1))
    return tree
