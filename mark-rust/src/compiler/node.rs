/*
    class Node:
    represents a single HTML element Eg. <div>

    special nodes:
        _document -> represents a plaintext node. Should always be valid HTML.
*/

use crate::require::require;
use std::fmt::Display;

pub struct Node {
    // source code for the node
    pub code: String,
    // HTML tag of node (Eg. div, span, p, etc.)
    pub tag: String,
    // the indentation level of node.
    pub indent: usize,
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
        write!(fmt, "[{}] <{}> {}", self.indent, self.tag, inner)
    }
}

impl Node {
    pub fn new(code: &str) -> Self {
        let trimmed = code.trim();
        let split: Vec<String> = trimmed.split_whitespace().map(str::to_string).collect();
        let tag;
        let mut inner = "";
        if is_string_line(String::from(trimmed)) {
            tag = String::from("_document");
            inner = rm_first_last(trimmed);
        } else {
            tag = split[0].clone();
        }
        if tag == "require" {
            return require(tag);
        }
        return Node {
            code: String::from(code),
            tag,
            indent: crate::utils::get_indent_level(String::from(code)),
            inner: String::from(inner),
        };
    }
    pub fn chain(&self, add_code: &str) -> Self {
        /*
            the chain method allows us to concatenate another
            piece of code to a node, allowing the usage of Mark's
            "and" statement.
        */
        let mut code = String::from(add_code.trim());
        code.replace_range(0..3, "");
        return Node::new(&(self.code.clone() + &code));
    }
    pub fn document(code: &str, inner: &str) -> Self {
        /*
            Similar to the new() implementation,
            but specific to document nodes.
            Typically used for plaintext, JavaScript,
            CSS, and HTML.
        */
        return Node {
            code: String::new(),
            tag: String::from("_document"),
            indent: crate::utils::get_indent_level(String::from(code)),
            inner: String::from(inner),
        };
    }
    pub fn opening_tag(&self) -> String {
        /*
            returns the opening tag of the node.
            (Eg. <div id="logo">)
        */
        if self.tag == "_document" {
            return String::from(format!("{}", self.inner));
        }
        return String::from(format!("<{}{}>", self.tag, self.attributes()));
    }
    pub fn closing_tag(&self) -> String {
        /*
            returns the closing tag of the node.
            (Eg. </div>)
        */
        if self.tag == "_document" {
            return String::from("");
        }
        return String::from(format!("</{}>", self.tag));
    }
}
