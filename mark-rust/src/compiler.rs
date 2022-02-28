use std::fs;
mod errs;
mod remove_comments;

pub fn compile(filename: String) {
    println!("Compiling {}", filename);
    let mut contents =
        fs::read_to_string("test.mark").expect(errs.throw("Could not read file, does it exist?"));
    contents = remove_comments::remove_comments(contents.clone());
    let content_lines = contents.lines();
    for (_, line) in content_lines.enumerate() {
        println!("{}", line);
    }
}
