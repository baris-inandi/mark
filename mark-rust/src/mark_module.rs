mod to_html;
use crate::compiler::node::Node;

pub struct MarkModule {
    pub path: String,
    pub nodelist: Vec<Node>,
}

impl MarkModule {
    pub fn new(path: String, nodelist: Vec<Node>) -> Self {
        let mut padded_nodelist = nodelist;
        padded_nodelist.push(Node::new("_eof"));
        return MarkModule {
            path,
            nodelist: padded_nodelist,
        };
    }
}
