pub fn parse_lines(code: String) {
    for line in code.lines() {
        let trimmed = line.trim().to_string();

        // skip empty lines
        if trimmed == "" {
            continue;
        }

        let new_node = super::node::Node::new(line);
        println!("{}", new_node);
    }
}
