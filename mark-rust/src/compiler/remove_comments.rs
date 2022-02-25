struct MarkStringContext {
    in_block: bool,  // `string`
    in_single: bool, // 'string'
    in_double: bool, // "string"
}

impl MarkStringContext {
    fn new() -> MarkStringContext {
        MarkStringContext {
            in_block: false,
            in_single: false,
            in_double: false,
        }
    }
    fn in_string(&self) -> bool {
        self.in_block || self.in_single || self.in_double
    }
    fn update(&mut self, c: char) {
        if c == '"' {
            self.in_double = !self.in_double;
        } else if c == '\'' {
            self.in_single = !self.in_single;
        } else if c == '`' {
            self.in_block = !self.in_block;
        }
    }
}

pub fn remove_comments(code: String) -> String {
    // removes all comments from source code:
    // mark uses // for oneline comments, terminated with a newline
    // mark uses /* */ for multiline comments, terminated with a */
    // chars inside mark strings (", ', and `) are ignored.
    let mut comment_oneline = false; // // ...
    let mut comment_multiline = false; // /* ... */
    let mut new_code: Vec<String> = Vec::new();
    let mut string_context = MarkStringContext::new();
    for line in code.lines() {
        for (index, c) in line.chars().enumerate() {
            string_context.update(c);
            let mut l = line.to_owned();
            l.push(' ');
            let mut new_line = String::new();
            if c == '/' && !string_context.in_string() {
                let next_char = l.chars().nth(index + 1).unwrap();
                if next_char == '/' {
                    // oneline comment opening
                    comment_oneline = true;
                } else if next_char == '*' {
                    // multiline comment opening
                    comment_multiline = true;
                }
            } else if c == '\n' {
                // terminate oneline comment
                comment_oneline = false;
            } else if c == '*' && !string_context.in_string() {
                let next_char = l.chars().nth(index + 1).unwrap();
                if next_char == '/' {
                    // terminate multiline comment
                    comment_multiline = false;
                }
            }
            if !comment_oneline && !comment_multiline {
                new_line.push(c);
            }
            new_code.push(new_line);
        }
    }
    return new_code.join("");
}
