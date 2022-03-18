mod attributes;
mod block;
pub mod node;
pub mod parse_mark;
pub mod preprocess;

pub fn compile_string(code: &str) -> String {
    return parse_mark::parse(String::from(code), "<anonymous>");
}
