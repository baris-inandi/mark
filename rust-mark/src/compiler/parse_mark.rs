mod comment_context;
mod remove_comments;
mod string_context;

use super::block::block;
use super::node::Node;
use comment_context::MarkCommentContext;
use string_context::MarkStringContext;

fn add_to_dom(dom: &mut Vec<Node>, node: Node) {
    dom.push(node);
}

pub fn parse(code: &str, filename: &str) -> String {
    /*
        Parses Mark code, returns DOM
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
            let (n, s) = block(&line, trimmed, &code, idx);
            skip_buffer += s;
            add_to_dom(&mut dom, n);
        } else if trimmed.starts_with("and ") || trimmed.starts_with("and\n") {
            // handle "and" statement
            let n = dom[dom.len() - 1].chain(&trimmed);
            dom.pop();
            add_to_dom(&mut dom, n);
        } else {
            add_to_dom(&mut dom, Node::new(&line));
        }
    }

    /*
        After generating an indented nodelist, convert to HTML
    */
    println!("SOURCE {:?}", &filename);
    for i in &dom {
        println!("{}", i);
    }
    return String::new();
}
