from src.lib.lang import minify
from src.classes.node import Node
from src.lib.lang import styling
from src import config


def handle_block_node(lines, block_start, index, block_decleration,
                      block_name_indentation) -> Node:
    block_inner = "\n".join(lines[block_start + 1:index - 1])
    if block_decleration.strip().startswith("text"):
        # Plaintext block
        n = Node("_plaintext_block", block_start + 1)
        n.block_inner = block_inner
        n.indent = block_name_indentation
        return n
    elif block_decleration.strip().startswith("script"):
        if config.MINIFY:
            block_inner = minify.js(block_inner)
    elif block_decleration.strip().startswith("style"):
        # the below line throws an error if the language is not supported
        # no need to validate again
        styling_lang = styling.get_styling_language(block_decleration)
        # sass/scss/less preprocessing
        # styling.to_css() also minifies in the process,
        # so no need for minify.css()
        if styling_lang in ["sass", "scss", "less"]:
            block_inner = styling.to_css(block_inner, styling_lang)
        else:
            if config.MINIFY:
                block_inner = minify.css(block_inner)
    n = Node(block_decleration[:-1], block_start + 1)
    n.block_inner = block_inner
    n.indent = block_name_indentation
    return n
