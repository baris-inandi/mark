use crate::compiler::remove_comments;
use crate::compiler::{compile_string, node::Node, preprocess::get_preprocess_inner_html};
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
    let mut ext = filename_dot_split[filename_dot_split.len() - 1];
    let contents = remove_comments::remove_comments(f);
    match ext {
        "mark" => {
            return Node::document(code, &compile_string(&contents));
        }
        &_ => {
            // .js should be parsed with processor "script", so change variable ext.
            if vec!["js", "cjs"].contains(&ext) {
                ext = "script";
            } else if ext == "mjs" {
                ext = "module";
            } else if ext == "css" {
                ext = "style";
            }
            let inner = get_preprocess_inner_html(contents, String::from(ext));
            return Node::document(code, &inner);
        }
    }
}
