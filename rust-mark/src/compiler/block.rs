use super::node::Node;
use super::preprocess::preprocess;

pub fn block(line: &str, trimmed_line: String, code: String, block_idx: usize) -> (Node, usize) {
    /*
        Handles blocks. Eg. script`console.log("hi")`
        Handlers are defined in the hashmap below.
        All block strings are passed to the corresponding handler
        and a _document node is returned.
    */
    let code_after_block_vector = code.lines().collect::<Vec<&str>>();
    let code_after_block = code_after_block_vector[block_idx..].join("\n");
    let mut block_inner = String::new();
    let mut opening_backtick_found = false;
    let block_split: Vec<&str> = trimmed_line.split("`").collect();
    let block_annotation = block_split[0];
    let mut skip_lines: usize = 0;
    for line in code_after_block.lines() {
        if line.contains("`") && opening_backtick_found {
            break;
        }
        block_inner += line;
        block_inner += "\n";
        skip_lines += 1;
        opening_backtick_found = true;
    }
    block_inner = block_inner.trim().to_string();
    block_inner.replace_range(0..block_annotation.len() + 1, "");

    return (
        preprocess(line, block_inner, String::from(block_annotation)),
        skip_lines,
    );
}
