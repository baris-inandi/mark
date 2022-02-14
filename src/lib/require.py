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
from src import config
from src.lib.parser.read_code_file import read_code_file


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


def require_markdown(uri: str):
    try:
        import markdown
        with open(uri) as f:
            return markdown.markdown(f.read())
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
        n = Node("_document", line_number)
        n.indent, n.block_inner = indent, require_html(uri)
        return n
    elif ext == "md":
        n = Node("_document", line_number)
        n.indent, n.block_inner = indent, require_markdown(uri)
        return n
    elif ext == config.extension:
        n = Node("_module", line_number)
        n.indent, n.block_inner = indent, read_code_file(uri, True)
        return n
    else:
        throw([
            f'Unexpected filetype in require statement: ".{ext}"',
            'Require only accepts the following filetypes:',
            f'.js .css .sass .scss .less .html .htm .md .{config.extension}',
        ],
              docs="require")
