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

from mark.utils.error import throw, error_line
from mark.utils.utils import indentation_level
from mark.compiler.classes.node import Node
from mark.compiler.lang import css_preprocessor
from termcolor import colored
from mark.compiler.require.external_require import external_require
from mark.compiler.lang import minify
from os import getcwd
from mark.config import config


def require_preprocessor(uri: str, lang: str):
    try:
        with open(uri) as f:
            out = css_preprocessor.to_css(f.read(), lang, uri)
            return f"<style>{out.strip()}</style>"
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
    indent = indentation_level(line)
    line = line.strip()
    split = line.split("attr", 1)
    error_line(line_number)

    if len(split) > 1:
        throw("Require doesn't accept any attributes", docs="require")

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
        out = minify.js(require_plaintext_file(uri))
        if config.user["minify"]:
            out = minify.js(out)
        n.block_inner = f'<script>{out}</script>'
        return n
    elif ext == "css":
        n = Node("_document", line_number)
        n.indent = indent
        out = minify.css(require_plaintext_file(uri))
        if config.user["minify"]:
            out = minify.css(out)
        n.block_inner = f'<style>{out}</style>'
        return n
    elif ext in ["scss", "sass", "less"]:
        n = Node("_document", line_number)
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
