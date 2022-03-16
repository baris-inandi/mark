pub mod compiler;
pub mod errs;
pub mod mark_module;
pub mod require;
pub mod utils;

fn main() {
    compiler::compile_string("require test.mark");
}
