use super::node::Node;

fn sass(code: String) -> Node {
    return Node::new(&code);
}

fn scss(code: String) -> Node {
    return Node::new(&code);
}

fn markdown(code: String) -> Node {
    return Node::new(&code);
}

fn less(code: String) -> Node {
    return Node::new(&code);
}

pub fn preprocess(code: String, processor: String) -> Node {
    if processor == "sass" {
        return sass(code);
    } else if processor == "scss" {
        return scss(code);
    } else if processor == "md" {
        return markdown(code);
    } else if processor == "less" {
        return less(code);
    } else {
        return Node::new(&code);
    }
}
