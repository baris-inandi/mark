use super::node::Node;

/*
    Requires no compilation step
*/

fn wrap_style(code: String) -> String {
    return format!("<s>{}</style>", code);
}

fn wrap_script(code: String) -> String {
    return format!("<script>{}</script>", code);
}

/*
    Requires compilation step
*/

fn sass(code: String) -> String {
    return wrap_style(code);
}

fn scss(code: String) -> String {
    return wrap_style(code);
}

fn markdown(code: String) -> String {
    return code;
}

pub fn preprocess(line: &str, code: String, processor: String) -> Node {
    // JavaScript, CSS, HTML, and plaintext should always be handled as plaintext
    let inner;
    if processor == "" {
        inner = code;
    } else if processor == "script" {
        inner = wrap_script(code);
    } else if processor == "style" {
        inner = wrap_style(code);
    } else if processor == "sass" {
        inner = sass(code);
    } else if processor == "scss" {
        inner = scss(code);
    } else if processor == "md" {
        inner = markdown(code);
    } else {
        inner = String::new();
        crate::errs::throw("Unknown block annotation");
    }
    return Node::document(line, inner.as_str());
}
