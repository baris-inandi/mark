mod compiler;
pub mod errs;
pub mod node;
pub mod utils;

fn main() {
    compiler::compile(String::from("test.mark"));
}
