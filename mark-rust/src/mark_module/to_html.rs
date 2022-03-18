use super::MarkModule;

impl MarkModule {
    pub fn to_html(&self) -> String {
        let mut out = String::new();
        let mut stack: Vec<String> = Vec::new();
        let tab_width = 2;
        for (idx, n) in self.nodelist.iter().enumerate() {
            if n.tag == "_eof" {
                break;
            }
            let n_next = &self.nodelist[idx + 1];
            out += n.opening_tag().as_str();
            stack.push(n.closing_tag());
            if n.indent >= n_next.indent {
                out += n.closing_tag().as_str();
            }
            if n.indent < n_next.indent {
                let indent_difference = n_next.indent - n.indent;
                if indent_difference % tab_width != 0 {
                    crate::errs::throw("Indentation error");
                }
            } else if n.indent > n_next.indent {
                let mut indent_difference = n.indent - n_next.indent;
                if indent_difference % tab_width != 0 {
                    crate::errs::throw("Indentation error");
                }
                indent_difference /= tab_width;
                for _ in 0..indent_difference {
                    stack.pop();
                    out += stack[stack.len() - 1].as_str();
                }
                /*                 for i in &stack {
                    print!("{}", i);
                }
                println!("") */
            }
        }
        stack.reverse();
        /*         for i in &stack {
            print!("{}", i);
        } */
        println!("");
        for close_node in &stack {
            out += close_node.as_str();
        }
        return out;
    }
}
