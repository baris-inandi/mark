// use std::fs;
mod node;

fn main() {
    println!("Hello, world!");
    let x = node::Node::new("div .hi".to_string());
    println!("{}", x.tag);
    /*     let filename = "hello.txt";
    println!("In file {}", filename);
    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");
    println!("With text:\n{}", contents);
    let content_lines = contents.lines();
    for i in content_lines {
        println!("{}", i);
        println!("{}", i.len());
    } */
}
