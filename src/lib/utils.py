from os import getcwd, path, chdir


def indentation_level(line: str) -> int:
    return len(line) - len(line.lstrip())


def minimal_indentation(lines: list[str]) -> list[str]:
    line_indent_indices = [
        len(line) - len(line.lstrip()) for line in lines if line.strip() != ""
    ]
    remove_level = min(line_indent_indices)
    lines = list(map(lambda line: line[remove_level:], lines))
    return lines


def set_wd(filepath: str) -> None:
    chdir(path.dirname(path.join(getcwd(), filepath)))
