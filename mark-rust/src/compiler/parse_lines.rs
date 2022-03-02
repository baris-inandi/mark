struct MarkVirtualDOM {
    nodes: Vec<super::node::MarkNode>,
    _module: String,
}

impl MarkVirtualDOM {
    fn new(module: String) -> MarkVirtualDOM {
        MarkVirtualDOM {
            nodes: Vec::new(),
            _module: module,
        }
    }
    fn new_node(&mut self, line: String) {
        /*
        gets a Mark code line and appends the
        newly generated Node to MarkVirtualDOM.nodes
        */
        self.nodes.push(super::node::MarkNode::new(line));
    }
}

pub fn parse_lines(code: String, filename: String) {
    let mut dom = MarkVirtualDOM::new(filename);
    for line in code.lines() {
        dom.new_node(String::from(line));
        // trimmed line with no indentation and \n
        let trimmed = line.trim().to_string();

        // skip empty lines
        if trimmed == "" {
            continue;
        }

        // whitespace-separated line
        let separated: Vec<String> = trimmed.split_whitespace().map(|s| s.to_string()).collect();
        // keyword, can be a reserved one like require or a node like <div />
        let kw = separated.get(0).unwrap();
        println!("{}", kw);
    }
}
