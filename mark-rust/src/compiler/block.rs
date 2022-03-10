use super::node::Node;
use super::preprocess::preprocess;

fn plaintext_block(block: String) -> Node {
    let n = Node::new(block.as_str());
    n.tag = String::from("_document");
    n.inner = block;
    return n;
}

pub fn block(trimmed_code: String) -> Node {
    /*
        Handles blocks. Eg. script`console.log("hi")`
        Handlers are defined in the hashmap below.
        All block strings are passed to the corresponding handler
        and a _document node is returned.
    */
    let block_split: Vec<&str> = trimmed_code.split("`").collect();
    println!("{}", block_split.len());
    let block_annotation = block_split[0];
    // JavaScript, CSS, HTML, and plaintext should always be handled as plaintext
    if vec!["script", "style", "html", ""].contains(&block_annotation) {
        return plaintext_block(trimmed_code);
    }
    return preprocess(String::from(&trimmed_code), String::from(block_annotation));
}
