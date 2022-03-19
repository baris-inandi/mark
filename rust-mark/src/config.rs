use lazy_static::lazy_static;
use std::fs;
use std::sync::atomic::{AtomicBool, AtomicU64, Ordering};

const DEFAULT_INDENT: u64 = 2;
const DEFAULT_MINIFY: bool = false;

// global variable
lazy_static! {
    static ref MINIFY: AtomicBool = AtomicBool::new(DEFAULT_MINIFY);
    static ref INDENT: AtomicU64 = AtomicU64::new(DEFAULT_INDENT);
}

pub fn mark_init() {
    fs::File::create(
        r#"
{
    "name": "New Mark Project",
    "package": [{ "from": "index.mark", "to": "dist/index.html" }]
}
    "#,
    )
    .unwrap();
}

pub fn load_config() {
    // Some JSON input data as a &str. Maybe this comes from the user.
    let data = fs::read_to_string("mark.json").unwrap_or_else(|_| {
        return crate::errs::throw("Could not read mark.json, does it exist?");
    });

    // Parse the string of data into serde_json::Value.
    let v: serde_json::Value = serde_json::from_str(&data).unwrap();

    // always ensure the package key for compilation.
    if !v["package"].is_array() {
        crate::errs::throw("key \"package\" in mark.json should be an array");
    }

    let minify_conf = match v.get("minify") {
        Some(minify_conf) => minify_conf.as_bool().unwrap_or(DEFAULT_MINIFY),
        None => DEFAULT_MINIFY,
    };
    let indent_conf = match v.get("indent") {
        Some(indent_conf) => indent_conf.as_u64().unwrap_or(DEFAULT_INDENT),
        None => DEFAULT_INDENT,
    };

    INDENT.store(indent_conf, Ordering::Relaxed);
    MINIFY.store(minify_conf, Ordering::Relaxed);
}

pub fn get_indent() -> u64 {
    return INDENT.load(Ordering::Relaxed);
}

pub fn get_minify() -> bool {
    return MINIFY.load(Ordering::Relaxed);
}
