/* pub fn remove_comments(code: String) -> String {
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
            if index < line.len() {
                if char == '/' && !in_comment {
                    let next_char = line.chars().nth(index + 1).unwrap();
                    if next_char == '/' {
                        in_oneline = true;
                        in_comment = true;
                    } else if next_char == '*' {
                        in_multiline = true;
                        in_comment = true;
                    }
                }
                if in_multiline {
                    if char == '*' {
                        let next_char = line.chars().nth(index + 1).unwrap();
                        if next_char == '/' {
                            in_multiline = false;
                            in_comment = false;
                        }
                    }
                }
            }
            if in_oneline {
                if char == '\n' {
                    in_oneline = false;
                    in_comment = false;
                }
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
 */

pub fn remove_comments(source: String) -> String {
    let mut code = source.to_owned();
    code.push_str("\n");
    for (index, c) in code.chars().enumerate() {
        println!("{} {}", index, c);
    }
    return code;
}
