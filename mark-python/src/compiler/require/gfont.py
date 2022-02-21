from src.utils.error import throw, error_line
from src.classes.node import Node
from src.utils.utils import indentation_level
import urllib.parse


def gfont(line: str, line_number: int) -> Node:
    # analyze line
    error_line(line_number)
    indent = indentation_level(line)
    line = line.strip()
    split = line.split("attr", 1)

    if len(split) > 1:
        throw("gfont doesn't accept any attributes", docs="gfont")

    args = split[0].split(":")
    name = args[0][len("gfont"):].strip()

    if len(args) != 2:
        throw([
            "gfont should specify a font name",
            "and a comma-seperated list of required weights.",
            "Example: gfont Roboto: 300,400,500,700"
        ],
              docs="gfont")

    weights = args[1].strip().replace(",", ";")
    name = urllib.parse.quote(name)
    uri = f"css2?family={name}:wght@{weights}&display=swap"
    font_url = f'<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/{uri}" rel="stylesheet">'  # noqa

    n = Node("_document", line_number)
    n.block_inner = font_url
    n.indent = indent
    return n
