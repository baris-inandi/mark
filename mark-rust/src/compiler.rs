use std::fs;
mod attributes;
mod block;
pub mod node;
pub mod parse_lines;
pub mod preprocess;
pub mod remove_comments;

pub fn compile_string(code: &str) -> String {
    return parse_lines::parse_lines(String::from(code), "<anonymous>");
}

pub fn compile_file(filename: &str) -> String {
    let f = match fs::read_to_string(filename) {
        Ok(f) => f,
        Err(_) => crate::errs::throw("Could not read file, does it exist?"),
    };
    let contents = remove_comments::remove_comments(f);
    return parse_lines::parse_lines(contents, filename);
}
