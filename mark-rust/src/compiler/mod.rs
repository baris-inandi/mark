use std::fs;
use std::path::Path;
mod remove_comments;

pub fn compile(filename: String) {
    if Path::new(&filename).is_file() {
        crate::errs::throw("Could not read file, does it exist?");
    }
    let c: Result<String, std::io::Error> = fs::read_to_string(filename);

    // TODO:
    contents = remove_comments::remove_comments(contents.clone());
    let content_lines = contents.lines();
    for (_, line) in content_lines.enumerate() {
        println!("{}", line);
    }
}
