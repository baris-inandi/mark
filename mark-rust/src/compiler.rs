use std::fs;
mod remove_comments;

pub fn compile(filename: String) {
    let f = match fs::read_to_string(filename) {
        Ok(file) => file,
        Err(_) => crate::errs::throw("Could not read file, does it exist?"),
    };
    let contents = remove_comments::remove_comments(f);
    let content_lines = contents.lines();
    for (_, line) in content_lines.enumerate() {
        println!("{}", line);
    }
}
