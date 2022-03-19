// use crate::caching;
use crate::compiler::{node::Node, parse_mark, preprocess::get_preprocess_inner_html};
use std::fs;

pub fn require(code: &str) -> Node {
    // compiles and creates cache if not cached,
    // returns the cached code if cached.
    let trimmed = code.trim();
    let mut split_whitespace: Vec<&str> = trimmed.split_whitespace().collect();
    split_whitespace.remove(0);
    if split_whitespace.len() != 1 {
        crate::errs::throw("require only accepts one argument");
    }
    let filename = split_whitespace[0];
    let contents = match fs::read_to_string(filename) {
        Ok(contents) => contents,
        Err(_) => crate::errs::throw("Could not read file, does it exist?"),
    };
    /*
       // create new cache instance
       let cache = caching::MarkCache::new(filename.to_string()).unwrap();
       // return cached value if available
       if let Ok(cached_code) = cache.get_if_cached() {
           println!("USING CACHED CODE");
           return Node::document(code, &cached_code);
       }
    */
    let filename_dot_split: Vec<&str> = filename.split(".").collect();
    let mut ext = filename_dot_split[filename_dot_split.len() - 1];
    match ext {
        "mark" => {
            let compiled = parse_mark::parse(&contents, &filename);
            // cache.update(&compiled).unwrap();
            return Node::document(code, &compiled);
        }
        &_ => {
            // .js should be parsed with processor "script", so change variable ext.
            if vec!["js", "cjs"].contains(&ext) {
                ext = "script";
            } else if ext == "mjs" {
                ext = "module";
            } else if ext == "css" {
                ext = "style";
            }
            let inner = get_preprocess_inner_html(contents, String::from(ext));
            // cache.update(&inner).unwrap();
            return Node::document(code, &inner);
        }
    }
}
