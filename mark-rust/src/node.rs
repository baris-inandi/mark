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
        Node {
            code: code.clone(),
            tag: code.split_whitespace().collect(),
            line_number: 0,
            indent: 0,
            attrs: "".to_string(),
            inner: "".to_string(),
        }
    }
}
