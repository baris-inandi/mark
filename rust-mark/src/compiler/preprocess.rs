use super::node::Node;

fn sass(code: String, _flavor: String) -> String {
    let code_processed = &code;
    return format!("<style>{}</style>", code_processed);
}

pub fn get_preprocess_inner_html(code: String, processor: String) -> String {
    let inner;
    if processor == "" {
        inner = code;
    } else if processor == "script" {
        inner = format!("<script>{}</script>", code);
    } else if processor == "module" {
        inner = format!("<script type=\"module\">{}</script>", code);
    } else if processor == "style" {
        inner = format!("<style>{}</style>", code);
    } else if processor == "sass" {
        inner = sass(code, processor);
    } else if processor == "scss" {
        inner = sass(code, processor);
    } else if processor == "python" {
        inner = format!("<py-script>{}</py-script>", code);
    } else if processor == "md" {
        inner = format!("<div class=\"mark-md\">{}</div>", code);
    } else {
        inner = String::new();
        crate::errs::throw(&format!("Cannot parse type {}", processor));
    }
    return inner;
}

pub fn preprocess(line: &str, code: String, processor: String) -> Node {
    // JavaScript, CSS, HTML, and plaintext should always be handled as plaintext
    let inner = get_preprocess_inner_html(code, processor);
    return Node::document(line, inner.as_str());
}
