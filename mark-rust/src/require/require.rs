use crate::compiler::node::Node;
use crate::compiler::remove_comments;
use std::fs;

pub fn require(code: &str) -> Node {
    // compiles and creates cache if not cached,
    // returns the cached code if cached.
    let trimmed = code.trim();
    let mut split_whitespace: Vec<&str> = trimmed.split_whitespace().collect();
    split_whitespace.remove(0);
    if split_whitespace.len() != 1 {
        crate::errs::throw("require only accepts one argument");
    }
    let filename = split_whitespace[0];
    let f = match fs::read_to_string(filename) {
        Ok(f) => f,
        Err(_) => crate::errs::throw("Could not read file, does it exist?"),
    };
    let filename_dot_split: Vec<&str> = filename.split(".").collect();
    let extension = filename_dot_split[filename_dot_split.len() - 1];
    let contents = remove_comments::remove_comments(f);
    match extension {
        "mark" -> 
    }
    return Node::document(code, "<div>out</div>");
}
