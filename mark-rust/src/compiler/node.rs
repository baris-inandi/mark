use std::fmt::Display;

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

impl Display for Node {
    fn fmt(&self, fmt: &mut std::fmt::Formatter) -> std::result::Result<(), std::fmt::Error> {
        write!(fmt, "[{}:{}] <{}>", self.line_number, self.indent, self.tag)
    }
}

impl Node {
    pub fn new(code: &str) -> Self {
        let trimmed = code.trim().to_string();
        let split: Vec<String> = trimmed.split_whitespace().map(str::to_string).collect();
        let new_node = Node {
            code: String::from(code),
            tag: split[0].clone(),
            line_number: 0,
            indent: crate::utils::get_indent_level(String::from(code)),
            attrs: String::new(),
            inner: String::new(),
        };
        return new_node;
    }
}

/*
        // whitespace-separated line
        let separated: Vec<String> = trimmed.split_whitespace().map(|s| s.to_string()).collect();
        // keyword, can be a reserved one like require or a node like <div />
        let kw = separated.get(0).unwrap();
*/
