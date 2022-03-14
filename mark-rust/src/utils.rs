extern crate base64;
use base64::decode;

pub fn get_indent_level(code: String) -> usize {
    let code = str::replace(&code, "\t", "    ");
    return code.chars().take_while(|c| c == &' ').count();
}

pub fn b64encode(path: &str) -> String {
    use base64::encode;
    return encode(path.as_bytes());
}

pub fn b64decode(e: &str) -> String {
    return String::from_utf8_lossy(&decode(e).unwrap()[..]).to_string();
}
