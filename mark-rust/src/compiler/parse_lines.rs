use std::collections::HashMap;

pub fn parse_lines(code: String) {
    for line in code.lines() {
        let trimmed = line.trim().to_string();

        // skip empty lines
        if trimmed == "" {
            continue;
        }

        if trimmed.contains("`") {
            let block_split: Vec<&str> = trimmed.split("`").collect();
            println!("{}", block_split.len());
            let block_annotation = block_split[0];
            let blocks: HashMap<&str, dyn Fn<String, String>> = HashMap::from([
                ("script", |code| code),
                ("style", |code| code),
                ("sass", |code| code),
                ("scss", |code| code),
                ("less", |code| code),
                ("html", |code| code),
                ("md", |code| code),
            ]);
        }

        let new_node = super::node::Node::new(line);
        println!("{}", new_node);
    }
}
