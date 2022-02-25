pub fn remove_comments(code: String) -> String {
    let mut new_code = String::new();
    let mut in_comment = false;
    let mut in_oneline = false;
    let mut in_multiline = false;
    let mut in_double_quote = false;
    let mut in_single_quote = false;
    let mut in_block = false;
    for line in code.lines() {
        let mut new_line = String::new();
        for (index, char) in line.chars().enumerate() {
            if char == '"' && !(in_block && in_single_quote) {
                in_double_quote = !in_double_quote;
            } else if char == '\'' && !(in_block && in_double_quote) {
                in_single_quote = !in_single_quote;
            } else if char == '`' && !(in_double_quote && in_single_quote) {
                in_block = !in_block;
            }
            if in_block || in_double_quote || in_single_quote {
                continue;
            }
            if char == '/' && index < line.len() && !in_comment {
                let next_char = line.chars().nth(index + 1).unwrap();
                if next_char == '/' {
                    in_oneline = true;
                    in_comment = true;
                } else if next_char == '*' {
                    in_multiline = true;
                    in_comment = true;
                }
            }
            if in_oneline {
                if char == '\n' {
                    in_oneline = false;
                    in_comment = false;
                }
                continue;
            }
            if in_multiline {
                if char == '*' && index < line.len() {
                    let next_char = line.chars().nth(index + 1).unwrap();
                    if next_char == '/' {
                        in_multiline = false;
                        in_comment = false;
                    }
                }
                continue;
            }
            if in_multiline || in_oneline || in_comment {
                new_line.push(char);
                continue;
            }
            if !in_comment {
                new_line.push(char);
            }
        }
        new_code.push_str(&new_line);
        new_code.push_str("\n");
    }
    return new_code;
}

/*
def remove_comments(code) -> str:
    if type(code) == list:
        code = "".join(code)
    in_comment, oneline, multiline, skip_buffer = False, False, False, 0
    out = ""
    in_block, in_double_quote, in_single_quote = False, False, False
    for index, char in enumerate(code):
        if skip_buffer > 0:
            skip_buffer -= 1
            continue

        # only if we are not in a string
        if char == '"' and not (in_block or in_single_quote):
            if in_double_quote:
                in_double_quote = False
            else:
                in_double_quote = True
        elif char == "'" and not (in_block or in_double_quote):
            if in_single_quote:
                in_single_quote = False
            else:
                in_single_quote = True
        elif char == "`" and not (in_double_quote or in_single_quote):
            if in_block:
                in_block = False
            else:
                in_block = True

        if in_double_quote or in_single_quote or in_block:
            out += char
            continue

        # parse comments
        # // for oneline
        # /* for multiline
        if char == "/":
            if code[index + 1] == "/" and not in_comment:
                in_comment, oneline = True, True
            elif code[index + 1] == "*" and not in_comment:
                in_comment, multiline = True, True
                 if char == "\n" and oneline:
                     in_comment, oneline = False, False
                 if char == "*" and code[index + 1] == "/" and multiline:
                     in_comment, multiline = False, False
                     # skip the next two chars
                     # (which will certainly be */
)
            skip_buffer += 1
            continue
        if not in_comment:
            out += char
    return out

*/
