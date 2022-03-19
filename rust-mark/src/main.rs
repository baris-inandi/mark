use std::env;
pub mod caching;
pub mod compiler;
pub mod config;
pub mod errs;
pub mod mark_module;
pub mod require;
pub mod utils;

fn main() {
    config::load_config();
    let args: Vec<String> = env::args().collect();
    compiler::compile_string(&format!("require {}", &args[1]));
}
