from mark.utils.utils import indentation_level, minimal_indentation
from mark.compiler.lang.css_preprocessor import to_css
from mark.utils.error import throw
from mark.compiler.classes.node import Node


def handle_block(index: int,
                 lines: list[str]):  # returns a block node and a skipline
    i = index
    in_string = False
    string_inner = ""
    skip_index = 0
    join_char = "\n"
    css_preprocessor_lang = None
    block_tag = None
    if lines[index].strip().startswith("script`"):
        # will directly be passed to _document Node, no preprocessing
        block_tag = "script"
        pass
    elif lines[index].strip().startswith("style`"):
        # will directly be passed to _document Node, no preprocessing
        block_tag = "style"
        pass
    elif lines[index].strip().startswith("`"):
        # regular multiline string
        join_char = "<br/>"
    # css preprocessors
    elif lines[index].strip().startswith("sass`"):
        css_preprocessor_lang = "sass"
        block_tag = "style"
    elif lines[index].strip().startswith("scss`"):
        css_preprocessor_lang = "scss"
        block_tag = "style"
    elif lines[index].strip().startswith("less`"):
        css_preprocessor_lang = "less"
        block_tag = "style"
    else:
        throw("Unrecognized block type", docs="blocks")
    lines_after_block_start = "\n".join(lines[i:])
    for j, char in enumerate(lines_after_block_start):
        if char == "`" and not in_string:
            in_string = True
        elif char == "`" and in_string:
            in_string = False
            break
        if in_string and char != "`":
            string_inner += char
        if char == "\n":
            skip_index += 1
        if j == len(lines_after_block_start) - 1:
            throw(["Unclosed block found."], docs="blocks")
        i += 1
    string_inner = minimal_indentation(string_inner.split("\n"))
    if string_inner[0] == "":
        string_inner = string_inner[1:]
    if string_inner[-1] == "":
        string_inner = string_inner[:-1]
    string_inner = join_char.join(string_inner)
    if css_preprocessor_lang:
        string_inner = to_css(string_inner, css_preprocessor_lang)
    if block_tag:
        string_inner = f"<{block_tag}>{string_inner.strip()}</{block_tag}>"
    n = Node("_document", index)
    n.block_inner = string_inner
    n.indent = indentation_level(lines[index])
    return n, skip_index
