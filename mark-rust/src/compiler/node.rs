use std::fmt::Display;

pub struct Node {
    // source code for the node
    pub code: &mut String,
    // HTML tag of node (Eg. div, span, p, etc.)
    pub tag: &mut String,
    // The source code line number of the node
    pub line_number: usize,
    // the indentation level of node.
    pub indent: usize,
    // a string of attributes of node.
    pub attrs: &mut String,
    // the HTML of any _document Node
    // used only if the node is already in
    // HTML format.
    // (Eg. script and style blocks)
    pub inner: String,
}

fn is_string_line(line: String) -> bool {
    if (line.starts_with("\"") && line.ends_with("\""))
        || (line.starts_with("'") && line.ends_with("'"))
    {
        return true;
    }
    return false;
}

fn rm_first_last(value: &str) -> &str {
    let mut chars = value.chars();
    chars.next();
    chars.next_back();
    chars.as_str()
}

impl Display for Node {
    fn fmt(&self, fmt: &mut std::fmt::Formatter) -> std::result::Result<(), std::fmt::Error> {
        let inner = if self.inner.len() > 0 { "[...]" } else { "" };
        write!(
            fmt,
            "[{}:{}] <{}> {}",
            self.line_number, self.indent, self.tag, inner
        )
    }
}

impl Node {
    pub fn new(code: &str) -> Self {
        let trimmed = code.trim();
        let split: Vec<String> = trimmed
            .to_string()
            .split_whitespace()
            .map(str::to_string)
            .collect();
        let tag;
        let mut inner = "";
        if is_string_line(String::from(trimmed)) {
            tag = String::from("_document");
            inner = rm_first_last(trimmed);
        } else {
            tag = split[0].clone();
        }
        let new_node = Node {
            code: String::from(code),
            tag,
            line_number: 0,
            indent: crate::utils::get_indent_level(String::from(code)),
            attrs: String::new(),
            inner: String::from(inner),
        };
        return new_node;
    }
}
