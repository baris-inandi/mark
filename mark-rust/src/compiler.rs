use std::fs;
mod node;
mod parse_lines;
mod remove_comments;

pub fn compile(filename: String) {
    let f = match fs::read_to_string(&filename) {
        Ok(f) => f,
        Err(_) => crate::errs::throw("Could not read file, does it exist?"),
    };
    let contents = remove_comments::remove_comments(f);
    parse_lines::parse_lines(contents);
}
