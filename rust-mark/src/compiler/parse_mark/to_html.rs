use crate::compiler::node::Node;

pub fn nodelist_to_html(nodelist: &Vec<Node>) -> String {
    let mut out = String::new();
    let mut parent_stack: Vec<&str> = Vec::new();
    for (idx, node) in nodelist.iter().enumerate() {
        let next_node = match nodelist.get(idx + 1) {
            Some(node) => node,
            None => break, // TODO: this might effect the last node!!
        };
        println!("{}{}", node, next_node);
        if next_node.indent > node.indent {
            /*
                div
                    div
            */
            out += &format!("{}\n", node.get_opening_tag());
            parent_stack.push(&node.closing_tag);
        } else if next_node.indent < node.indent {
            /*
                    div
                div
            */
            out += &format!("{}\n", node.get_opening_tag());
            out += &format!("\n");
        } else {
            /*
                div
                div
            */
            out += &format!("{}\n", node.get_opening_tag());
        }
    }
    println!("\nOUT\n{}", out);
    return String::new();
}
