pub fn get_indent_level(code: String) -> usize {
    let code = str::replace(&code, "\t", "    ");
    return code.chars().take_while(|c| c == &' ').count();
}
