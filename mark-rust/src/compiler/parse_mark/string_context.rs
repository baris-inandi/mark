pub struct MarkStringContext {
    in_block: bool,  // `string`
    in_single: bool, // 'string'
    in_double: bool, // "string"
}

impl MarkStringContext {
    pub fn new() -> MarkStringContext {
        return MarkStringContext {
            in_block: false,
            in_single: false,
            in_double: false,
        };
    }
    pub fn in_string(&self) -> bool {
        self.in_block || self.in_single || self.in_double
    }
    pub fn update(&mut self, c: char) {
        if c == '"' {
            self.in_double = !self.in_double;
        } else if c == '\'' {
            self.in_single = !self.in_single;
        } else if c == '`' {
            self.in_block = !self.in_block;
        }
    }
}
