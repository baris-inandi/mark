use super::Node;

pub fn is_string_line(line: String) -> bool {
    if (line.starts_with("\"") && line.ends_with("\""))
        || (line.starts_with("'") && line.ends_with("'"))
    {
        return true;
    }
    return false;
}

pub fn rm_first_last(value: &str) -> &str {
    let mut chars = value.chars();
    chars.next();
    chars.next_back();
    chars.as_str()
}

impl Node {
    pub fn chain(&self, add_code: &str) -> Self {
        /*
            the chain method allows us to concatenate another
            piece of code to a node, allowing the usage of Mark's
            "and" statement.
        */
        let mut code = String::from(add_code.trim());
        code.replace_range(0..3, "");
        return Node::new(&(self.code.clone() + &code));
    }
    pub fn document(code: &str, inner: &str) -> Self {
        /*
            Similar to the new() implementation,
            but specific to document nodes.
            Typically used for plaintext, JavaScript,
            CSS, and HTML.
        */
        return Node {
            code: String::new(),
            tag: String::from("_document"),
            indent: crate::utils::get_indent_level(String::from(code)),
            inner: String::from(inner),
            closing_tag: String::new(),
        };
    }
    pub fn get_opening_tag(&self) -> String {
        /*
            returns the opening tag of the node.
            (Eg. <div id="logo">)
        */
        if self.tag == "_document" {
            return String::from(format!("{}", self.inner));
        }
        return String::from(format!("<{}{}>", self.tag, self.attributes()));
    }
}
