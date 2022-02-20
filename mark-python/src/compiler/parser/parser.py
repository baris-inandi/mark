from src.classes.node import Node
from src.utils.error import throw, error_file, error_line
from src.compiler.parser.handle_markup import handle_markup
from src.compiler.parser.read_code_file import read_code_file
from src.classes.dom import Dom
from src.compiler.parser.block import handle_block


def parse(lines: list[str], filename: str) -> list[Node]:
    """
    Gets parameter filename
    Parses code into a list of nodes.
    """

    error_file(filename)

    out: list[Node] = []
    skip_index = 0

    for index, line in enumerate(lines):
        if skip_index > 0:
            skip_index -= 1
            continue

        error_line(index)

        #################
        # Handle Blocks #
        #################
        if "`" in line:
            error_line(index + 1)
            block_node, skip_index = handle_block(index, lines)
            out.append(block_node)
            continue

        ##############
        # Line Skips #
        ##############
        if line.strip() == "":
            # skip if empty line
            continue

        #########
        # Nodes #
        #########
        out.append(handle_markup(out, line,
                                 index))  # handles plaintext and html elements

    for n in out:
        if n.tag == "_module":
            module_compiled = Dom(
                parse(read_code_file(n.block_inner, True),
                      n.block_inner)).to_html()
            n.block_inner, n.tag, n.line = module_compiled, "_document", ""

    return out
