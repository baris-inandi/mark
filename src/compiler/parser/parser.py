from src.classes.node import Node
from src.utils.error import throw, error_file, error_line
from src.compiler.parser.handle_markup import handle_markup
from src.compiler.parser.handle_block_node import handle_block_node
from src.utils.utils import indentation_level
from src.compiler.parser.read_code_file import read_code_file
from src.classes.dom import Dom


def is_block(test: str, tester: str) -> bool:
    return test.startswith(tester) and test.endswith(":")


def parse(lines: list[str], filename: str) -> list[Node]:
    """
    Gets parameter filename
    Parses code into a list of nodes.
    """

    error_file(filename)

    out: list[Node] = []
    block_start, skip_index = -1, 0

    for index, line in enumerate(lines):
        if skip_index > 0:
            skip_index -= 1
            continue

        error_line(index)

        ##########
        # Blocks #
        ##########
        end_line = lines[index - 1]
        if end_line.strip() == "end":
            # handle blocks Eg. script and style
            block_decleration = lines[block_start]
            block_indentation, end_indentation = indentation_level(
                block_decleration), indentation_level(end_line)
            if block_indentation != end_indentation:
                # Block and "end" should be in the same indentation level
                continue
            stripped_block = block_decleration.strip()
            if (is_block(stripped_block, "script")
                    or not is_block(stripped_block, "script")
                    and is_block(stripped_block, "style")):
                new_node = handle_block_node(lines, block_start, index,
                                             block_decleration,
                                             block_indentation)
                out.append(new_node)
            else:
                throw("Invalid block definition found.", docs="blocks")
            block_start = -1

        ##############
        # Line Skips #
        ##############
        if line.strip() == "" or block_start != -1 or line.strip().startswith(
                "end"):
            # skip if empty line, or in a block
            continue

        ################
        # Change index #
        ################
        if (line.strip().startswith("style") and line.strip().endswith(":")
            ) or (line.strip().startswith("script")
                  and line.strip().endswith(":")):
            block_start = index
            continue

        #########
        # Nodes #
        #########
        out.append(handle_markup(out, line,
                                 index))  # handles plaintext and html elements

    if block_start != -1:
        throw(["Unclosed block found.", "Use \"end\" to close a block"],
              docs="blocks")

    for n in out:
        if n.tag == "_module":
            module_compiled = Dom(
                parse(read_code_file(n.block_inner, True),
                      n.block_inner)).to_html()
            n.block_inner, n.tag, n.line = module_compiled, "_document", ""

    return out
