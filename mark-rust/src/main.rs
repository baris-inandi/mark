mod compiler;
pub mod errs;
pub mod utils;

fn main() {
    compiler::compile(String::from("test.mark"));
}
