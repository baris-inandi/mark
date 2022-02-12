def indentation_level(line: str) -> int:
    return len(line) - len(line.lstrip())


def minimal_indentation(lines: list[str]) -> str:
    line_indent_indices = [
        len(line) - len(line.lstrip()) for line in lines if line.strip() != ""
    ]
    remove_level = min(line_indent_indices)
    lines = list(map(lambda line: line[remove_level:], lines))
    return lines
