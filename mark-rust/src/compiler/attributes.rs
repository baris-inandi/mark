use super::node::Node;

impl Node {
    pub fn attributes(&self) -> String {
        let code = self.code.clone();
        let mut whitespace_sep = code.split_whitespace().collect::<Vec<&str>>();
        for i in &whitespace_sep {
            println!("{}", i);
        }
        // whitespace_sep.remove(0);
        return String::from(code);
    }
}
