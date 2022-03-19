pub fn throw(msg: &str) -> String {
    println!("ERROR: {}", msg);
    return String::from(msg);
}
