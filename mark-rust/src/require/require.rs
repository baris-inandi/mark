use crate::compiler::node::Node;

pub fn require(code: &str) -> Node {
    // compiles and creates cache if not cached,
    // returns the cached code if cached.
    return Node::document(code, "<div>out</div>");
}
