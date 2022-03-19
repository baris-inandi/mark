pub fn remove_comments_in_line(
    code: &str,
    string_context: &mut super::string_context::MarkStringContext,
    comment_context: &mut super::comment_context::MarkCommentContext,
) -> String {
    // removes all comments from given source code:
    // mark uses // for oneline comments, terminated with a newline
    // mark uses /* */ for multiline comments, terminated with a */
    // chars inside mark strings (", ', and `) are ignored.
    let mut new_code = String::new();
    let mut skip_buffer: u8 = 0;
    for (index, c) in code.chars().enumerate() {
        if skip_buffer > 0 {
            skip_buffer -= 1;
            continue;
        }
        string_context.update(c);
        if c == '\n' {
            /*
                newline is special in this case,
                it terminates every oneline comment.
                but to preserve line numbers,
                \n should always be pushed unconditionally.
            */
            // TODO: if oneline string is used in multiple lines, error out.
            new_code.push(c);
            comment_context.comment_oneline = false;
            continue;
        }
        let code = String::from(code) + "\n";
        if c == '/' && !string_context.in_string() {
            let next_char = code.chars().nth(index + 1).unwrap();
            if next_char == '/' {
                // oneline comment opening
                comment_context.comment_oneline = true;
            } else if next_char == '*' {
                // multiline comment opening
                comment_context.comment_multiline = true;
            }
        } else if c == '*' && !string_context.in_string() {
            let next_char = code.chars().nth(index + 1).unwrap();
            if next_char == '/' {
                // skip the next two chars since they will certainly be "*/"
                skip_buffer += 1;
                // terminate multiline comment
                comment_context.comment_multiline = false;
                // avoid appending next char
                continue;
            }
        }
        if !comment_context.comment_oneline && !comment_context.comment_multiline {
            new_code.push(c);
        }
    }
    comment_context.comment_oneline = false;
    return new_code;
}
