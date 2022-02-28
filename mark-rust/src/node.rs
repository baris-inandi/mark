pub struct Node {
    // source code for the node
    pub code: String,
    // HTML tag of node (Eg. div, span, p, etc.)
    pub tag: String,
    // The source code line number of the node
    pub line_number: usize,
    // the indentation level of node.
    pub indent: usize,
    // a string of attributes of node.
    pub attrs: String,
    // the HTML of any _document Node
    // used only if the node is already in
    // HTML format.
    // (Eg. script and style blocks)
    pub inner: String,
}

impl Node {
    pub fn new(code: String) -> Self {
        let node_tag: Vec<String> = code.split_whitespace().map(str::to_string).collect();
        println!("{:?}", node_tag[0]);
        let new_node = Node {
            code,
            tag: node_tag[0].clone(),
            line_number: 0,
            indent: 0,
            attrs: String::new(),
            inner: String::new(),
        };
        return new_node;
    }
}
