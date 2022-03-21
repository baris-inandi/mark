use crate::compiler::node::Node;

pub fn nodelist_to_html(nodelist: &mut Vec<Node>) -> String {
    let mut out = String::new();
    let mut parent_stack: Vec<&str> = Vec::new();
    nodelist.push(Node::eof());
    for (idx, node) in nodelist.iter().enumerate() {
        let next_node = match nodelist.get(idx + 1) {
            Some(node) => node,
            None => break,
        };
        if &node.tag == "_eof" {
            break;
        }
        if node.indent % crate::config::get_indent() as usize != 0 {
            crate::errs::throw("Indentation error");
        }
        out += &node.get_opening_tag();
        if next_node.indent > node.indent {
            /*
                div
                    div
            */
            // out += &format!("{}\n", next_node.get_opening_tag());
            parent_stack.push(&node.closing_tag);
        } else if next_node.indent < node.indent {
            /*
                    div
                div
            */
            out += &format!("{}\n", parent_stack[parent_stack.len() - 1]);
            parent_stack.pop();
        } else {
            /*
                div
                div
            */
            out += &format!("{}\n", node.get_opening_tag());
            out += &format!("{}\n", node.closing_tag);
            out += &format!("{}\n", next_node.get_opening_tag());
        }
        out += "\n";
    }
    parent_stack.reverse();
    for closing_tag in parent_stack {
        out += &format!("{}\n", closing_tag);
    }
    return out;
}
