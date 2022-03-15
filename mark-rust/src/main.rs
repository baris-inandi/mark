pub mod compiler;
pub mod errs;
pub mod mark_module;
pub mod utils;

fn main() {
    compiler::compile(String::from("test.mark"));
}
