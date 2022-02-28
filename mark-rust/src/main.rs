mod compiler;
pub mod errs;
pub mod node;

fn main() {
    compiler::compile(String::from("test.mark"));
}
