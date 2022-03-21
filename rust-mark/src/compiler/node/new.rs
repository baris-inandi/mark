use super::node_helpers;
use super::Node;
use crate::require::require::require;

impl Node {
    pub fn new(code: &str) -> Self {
        let trimmed = code.trim();
        let split: Vec<String> = trimmed.split_whitespace().map(str::to_string).collect();
        let tag;
        let mut inner = "";
        if node_helpers::is_string_line(String::from(trimmed)) {
            tag = String::from("_document");
            inner = node_helpers::rm_first_last(trimmed);
        } else {
            tag = split[0].clone();
        }
        if tag == "require" {
            return require(code);
        }
        return Node {
            code: String::from(code),
            tag: tag.clone(),
            indent: crate::utils::get_indent_level(String::from(code)),
            inner: String::from(inner),
            closing_tag: if tag == "_document" {
                String::new()
            } else {
                format!("</{}>", tag)
            },
        };
    }
}
