use std::env;
pub mod caching;
pub mod compiler;
pub mod config;
pub mod errs;
pub mod require;
pub mod utils;

fn main() {
    config::load_config();
    let args: Vec<String> = env::args().collect();
    let out = compiler::parse_mark::parse(&format!("require {}", &args[1]), "<anonymous>");
    println!("{}", out);
}
