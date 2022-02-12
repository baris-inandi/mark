from src.classes.node import Node
from src.lib.parser.remove_comments import remove_comments
from src.lib.error import throw, error_file
from src.lib.parser.handle_markup import handle_markup
from src.lib.parser.handle_block_node import handle_block_node
from src.lib.utils import indentation_level


def is_block(test: str, tester: str) -> bool:
    return test.startswith(tester) and test.endswith(":")


def parse(filename: str) -> list[Node]:
    """
    Gets parameter filename
    Parses code into a list of nodes.
    """

    with open(filename) as f:
        lines = remove_comments(f.read()).split("\n")

    out: list[Node] = []
    block_start = -1
    skip_index = 0

    for index, line in enumerate(lines):
        if skip_index > 0:
            skip_index -= 1
            continue

        error_file(filename)

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
        out = handle_markup(out, line, index)  # handles plaintext and nodes

    if block_start != -1:
        throw(["Unclosed block found.", "Use \"end\" to close a block"],
              docs="blocks")

    for i in out:
        i.parse_attr()
        # print(i.line, i.opening_tag())

    return out
