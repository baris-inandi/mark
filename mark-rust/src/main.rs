pub mod caching;
// pub mod compiler;
// pub mod errs;
// pub mod mark_module;
pub mod utils;

fn main() {
    caching::mark_cache::MarkCache::new("./test.mark");
    // compiler::compile(String::from("test.mark"));
}
