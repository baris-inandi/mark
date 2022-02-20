from src.compiler.require.require import require
from src.compiler.require.gfont import gfont
from src.classes.node import Node
from src.utils.utils import indentation_level


def handle_markup(nodes: list[Node], line: str, index: int):
    """
        Determines type of line
        Possible Cases:
            - extension statement (and .foo)
            - plaintext element ("foo")
            - node (<div />)
            - require statement (require foo)
    """
    code = line.strip()
    split_code = code.split(" ", 1)
    tag = split_code[0]
    props = split_code[-1]
    if tag == "and":
        # Extension statement
        # appends extension props to <Node>.code
        nodes[-1].code += f' {props}'
    elif code[0] in ["'", '"'] and code[-1] in ["'", '"']:
        # Plaintext
        new = Node("_plaintext", index + 1)
        new.block_inner = code[1:-1]
        new.indent = indentation_level(line)
        nodes.append(new)
    elif tag == "require":
        # Require statement
        nodes.append(require(line, index + 1))
    elif tag == "gfont":
        # Require statement
        nodes.append(gfont(line, index + 1))
    else:
        # regular node
        nodes.append(Node(line, index + 1))
    return nodes
