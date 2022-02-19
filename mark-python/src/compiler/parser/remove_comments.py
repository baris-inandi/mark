def remove_comments(code) -> str:
    if type(code) == list:
        code = "".join(code)
    in_comment, oneline, multiline, skip_buffer = False, False, False, 0
    out = ""
    for index, char in enumerate(code):
        if skip_buffer > 0:
            skip_buffer -= 1
            continue

        # parse comments
        # // for oneline
        # /* for multiline
        if char == "/":
            if code[index + 1] == "/" and not in_comment:
                in_comment, oneline = True, True
            elif code[index + 1] == "*" and not in_comment:
                in_comment, multiline = True, True

        # parse end-of-comments
        # \n ends comment for //
        # */ ends comment for /*
        if char == "\n" and oneline:
            in_comment, oneline = False, False
        if char == "*" and code[index + 1] == "/" and multiline:
            in_comment, multiline = False, False
            # skip the next two chars
            # (which will certainly be */)
            skip_buffer += 1
            continue
        if not in_comment:
            out += char
    return out
