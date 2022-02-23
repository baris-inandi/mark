struct Node {
    // source code for the node
    code: String,
    // HTML tag of node (Eg. div, span, p, etc.)
    tag: String,
    // The source code line number of the node
    line_number: usize,
    // the indentation level of node.
    indent: usize,
    // a string of attributes of node.
    attrs: String,
    // the HTML of any _document Node
    // used only if the node is already in
    // HTML format.
    // (Eg. script and style blocks)
    inner: String,
}

impl Node {
    fn new(code: String) -> Self {
        // example `code` param:
        // "div .class #id attr x='y'"
        Node {
            code: code,
            tag: code.split_whitespace().to_string(),
            // TODO: above line errors out
            line_number: 0,
            indent: 0,
            attrs: "".to_string(),
            inner: "".to_string(),
        }
    }
}

fn main() {
    let n = Node::new("hello".to_string());
    println!("{}", n.tag);
}

//let mut split = "some string 123 ffd".split("123");
