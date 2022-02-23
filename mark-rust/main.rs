use std::fs;

fn main() {
    // --snip--
    let filename = "hello.txt";
    println!("In file {}", filename);
    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");
    println!("With text:\n{}", contents);
    let content_lines = contents.lines();
    for i in content_lines {
        println!("{}", i);
        println!("{}", i.len());
    }
}
