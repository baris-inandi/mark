struct MarkLineContext {
    trimmed: Vec<String>,
    keyword: String
}

impl MarkLineContext {
    fn new(line: String) -> MarkLineContext {
        let trimmed = line.trim().to_string();
        let separated =  line.split_whitespace().map(|s| s.to_string()).collect();
        let kw = separated.nth(0).unwrap();
        MarkLineContext {
            keyword: trimmed[0].clone(),
        }
    }

pub fn parse_lines(code: String) {
    for line in code.lines() {
        let mut line_whitespace_sep = line.split_whitespace().collect();
        let line_trimmed =
        let kw = seperated.nth(0);
    }
}
