// use std::fs;
mod compiler;

fn main() {
    compiler::compile(String::from("test.mark"));
}
