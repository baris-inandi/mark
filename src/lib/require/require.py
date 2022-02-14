"""
    require
    a bundler for Mark.

    Require is a bundler that can be used to bundle up a set of files.

    scripts
      require foo.js
    styles
      require foo.css
      require foo.scss
      require foo.sass
      require foo.less
    markup
      require foo.html
      require foo.htm
      require foo.mark  <- should be a module
      require foo.md
    external
      refer to external_require.py
"""

from src.lib.error import throw
from src.classes.node import Node
from src.lib.lang import styling
from termcolor import colored
from src.lib.require.external_require import external_require
from src.lib.lang import minify
from os import getcwd
from src import config


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


def require_plaintext_file(uri: str):
    try:
        with open(uri) as f:
            return f.read()
    except FileNotFoundError:
        s = colored(uri, "yellow")
        throw([
            f"Require: File not found: {s}",
            f"in working directory: {getcwd()}"
        ],
              docs="require")


def require_markdown(uri: str):
    try:
        import markdown
        with open(uri) as f:
            try:
                return markdown.markdown(f.read())
            except Exception as e:
                throw("invalid Markdown: " + str(e))
    except FileNotFoundError:
        s = colored(uri, "yellow")
        throw([
            f"Require: File not found: {s}",
            f"in working directory: {getcwd()}"
        ],
              docs="require")


def require(line: str, line_number: int) -> Node:

    # analyze line
    indent = len(line) - len(line.lstrip())
    line = line.strip()
    split = line.split("attr", 1)

    if len(split) > 1:
        throw("Require doesn't not accept any attributes", docs="require")

    lhs = split[0].strip().split(" ")
    if len(lhs) < 2:
        throw("Require statement must specify a uri", docs="require")
    if len(lhs) > 2:
        throw("Require statement must have exactly one uri specified",
              docs="require")
    uri = lhs[1]

    if uri.startswith("@"):
        return external_require(uri, line_number, indent)

    # rhs = split[1].strip() if len(split) > 1 else ""
    ext = uri.split(".")[-1]

    # create a new element
    if ext == "js":
        n = Node("_document", line_number)
        n.indent = indent
        n.block_inner = minify.js(
            f"<script>{require_plaintext_file(uri)}</script>")
        return n
    elif ext == "css":
        n = Node("_document", line_number)
        n.indent = indent
        n.block_inner = minify.css(
            f"<style>{require_plaintext_file(uri)}</style>")
        return n
    elif ext in ["scss", "sass", "less"]:
        n = Node("style", line_number)
        n.indent, n.block_inner = indent, require_preprocessor(uri, ext)
        return n
    elif ext in ["html", "htm"]:
        n = Node("_document", line_number)
        n.indent, n.block_inner = indent, require_plaintext_file(uri)
        return n
    elif ext == "md":
        n = Node("_document", line_number)
        n.indent, n.block_inner = indent, require_markdown(uri)
        return n
    elif ext == config.EXTENSION:
        n = Node("_module", line_number)
        n.indent, n.block_inner = indent, uri
        return n
    else:
        throw([
            f'Unexpected filetype in require statement: ".{ext}"',
            'Require only accepts the following filetypes:',
            f'.js .css .sass .scss .less .html .htm .md .{config.EXTENSION}',
        ],
              docs="require")
