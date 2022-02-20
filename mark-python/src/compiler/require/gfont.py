def gfont(line: str, line_number: int):
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
