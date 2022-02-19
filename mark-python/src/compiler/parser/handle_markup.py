from src.compiler.require.require import require
from src.classes.node import Node
from src.utils.utils import indentation_level


def handle_markup(tree: list[Node], line: str, index: int):
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
        new = n
    elif tag == "require":
        # Require statement
        new = require(line, index + 1)
    else:
        # Node
        new = Node(line, index + 1)
    return new
