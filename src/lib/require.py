"""
    require
    for easy import of files.

    require index.js
        can be used as a shorthand instead of:
    script attr src="index.js"

    or

    require global.css
        can be used as a shorthand instead of:
    link attr rel="stylesheet" href="styles.css"
"""

from src.lib.error import throw
from src.classes.node import Node
from src.lib.lang import styling
from termcolor import colored


def require_preprocessor(uri: str, lang: str):
    try:
        with open(uri) as f:
            return styling.to_css(f.read(), lang, uri)
    except FileNotFoundError:
        s = colored(uri, "yellow")
        throw([
            f"Require: File not found: {s}",
            "Preprocessed files",
            "(.sass, .scss, .less)",
            "must be located on the local disk.",
        ],
              docs="require")


def require_html(uri: str):
    try:
        with open(uri) as f:
            return f.read()
    except FileNotFoundError:
        s = colored(uri, "yellow")
        throw([
            f"Require: File not found: {s}",
        ], docs="require")


def require(line: str, line_number: int) -> Node:

    # analyze line
    indent = len(line) - len(line.lstrip())
    line = line.strip()
    split = line.split("attr", 1)
    lhs = split[0].strip().split(" ")
    if len(lhs) < 2:
        throw("Require statement must specify a uri", docs="require")
    if len(lhs) > 2:
        throw("Require statement must have exactly one uri specified",
              docs="require")
    uri = lhs[1]
    rhs = split[1].strip() if len(split) > 1 else ""
    ext = uri.split(".")[-1]

    # create a new element
    if ext == "js":
        n = Node(f'script attr src="{uri}" {rhs}', line_number)
        n.indent = indent
        return n
    elif ext == "css":
        n = Node(f'link attr rel="stylesheet" href="{uri}" {rhs}', line_number)
        n.indent = indent
        return n
    elif ext in ["scss", "sass", "less"]:
        n = Node("style", line_number)
        n.indent, n.block_inner = indent, require_preprocessor(uri, ext)
        return n
    elif ext in ["html", "htm"]:
        n = Node("div .require-html", line_number)
        n.indent, n.block_inner = indent, require_html(uri)
        return n
    else:
        throw([
            f'Unexpected filetype in require statement: ".{ext}"',
            'Require only accepts the following filetypes:',
            '.js .css .sass .scss .less .html .htm',
        ],
              docs="require")
