pub fn parse_lines(code: String) {
    for line in code.lines() {
        // trimmed line with no indentation and \n
        let trimmed = line.trim().to_string();
        // whitespace-separated line
        let separated = line.split_whitespace().map(|s| s.to_string()).collect();
        // keyword, can be a reserved one like require or a node like <div />
        let kw = separated.nth(0).unwrap();
    }
}
