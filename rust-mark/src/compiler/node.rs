/*
    struct Node:
    represents a single HTML element Eg. <div>

    special nodes:
        _document -> represents a plaintext node. Should always be valid HTML.
        _eof -> represents the end of the file in a mark module.
*/

mod new;
mod node_helpers;

use std::fmt::Display;

pub struct Node {
    // source code for the node
    pub code: String,
    // HTML tag of node (Eg. div, span, p, etc.)
    pub tag: String,
    // the indentation level of node.
    pub indent: usize,
    /*
        the HTML of any _document Node
        used only if the node is already in
        valid HTML format.
        (Eg. script and style blocks)
    */
    pub inner: String,
    /*
        closing tag of node,
        This is not in impl Node because it will be the same
        for the lifetime of any given node as opposed to Node::opening_tag()
        which can give a different output if the .chain() method is used for
        the same node.
    */
    pub closing_tag: String,
}

impl Display for Node {
    fn fmt(&self, fmt: &mut std::fmt::Formatter) -> std::result::Result<(), std::fmt::Error> {
        write!(
            fmt,
            "⤷ {} <{}> {}",
            self.indent,
            self.tag,
            if self.inner.len() > 0 { "[...]" } else { "" }
        )
    }
}
