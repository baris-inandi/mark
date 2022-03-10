use super::block::block;
use super::node::Node;

pub fn parse_lines(code: String) {
    for line in code.lines() {
        let trimmed = line.trim().to_string();
        // skip empty lines
        if trimmed == "" {
            continue;
        }
        // handle blocks
        if trimmed.contains("`") {
            block(trimmed);
        }
        let new_node = Node::new(line);
        println!("{}", new_node);
    }
}
