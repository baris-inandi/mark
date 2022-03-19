mod comment_context;
mod remove_comments;
mod string_context;

use super::block::block;
use super::node::Node;
use crate::mark_module::MarkModule;
use comment_context::MarkCommentContext;
use string_context::MarkStringContext;

fn is_and_statement(line: &str) -> bool {
    return line.starts_with("and ") || line.starts_with("and\n");
}

pub fn parse(code: String, filename: &str) -> String {
    /*
        Parses Mark code
    */
    let mut skip_buffer: usize = 0;
    let mut dom: Vec<Node> = Vec::new();
    let mut string_context = MarkStringContext::new();
    let mut comment_context = MarkCommentContext::new();

    for (idx, line_with_comments) in code.lines().enumerate() {
        let line = remove_comments::remove_comments_in_line(
            line_with_comments,
            &mut string_context,
            &mut comment_context,
        );

        // skip lines if needed, most probably because of a block
        if skip_buffer > 0 {
            skip_buffer -= 1;
            continue;
        }

        let trimmed = line.trim().to_string();
        // skip empty lines
        if trimmed == "" {
            continue;
        }

        if trimmed.contains("`") {
            // handle blocks
            let (n, s) = block(&line, trimmed, code.clone(), idx);
            skip_buffer += s;
            dom.push(n);
        } else if is_and_statement(&trimmed) {
            // handle "and" statement
            let n = dom[dom.len() - 1].chain(&trimmed);
            dom.pop();
            dom.push(n);
        } else {
            dom.push(Node::new(&line));
        }

        // get nextline, and stop loop if we reached EOF
        let nextline = match code.lines().nth(idx + 1) {
            Some(l) => l.trim(),
            None => break,
        };
        if !is_and_statement(nextline) {
            println!(
                "{}{}",
                " ".repeat(dom[dom.len() - 1].indent),
                dom[dom.len() - 1].opening_tag()
            );
        }
    }
    /*
        After generating an indented nodelist, create a mark module
    */
    let mark_module = MarkModule::new(String::from(filename), dom);
    return mark_module.to_html();
}
