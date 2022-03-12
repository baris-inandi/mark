use super::node::Node;

impl Node {
    pub fn attributes(&self) -> String {
        let code = self.code.clone();
        let mut whitespace_sep = code.split_whitespace().collect::<Vec<&str>>();
        whitespace_sep.remove(0);
        let mut post_attr = false;
        let mut attrs = String::new();
        let mut classes = String::new();
        let mut id_already_specified = false;
        for val in whitespace_sep {
            if val == "attr" {
                post_attr = true;
                continue;
            }
            if !post_attr {
                if val.starts_with(".") {
                    let mut val_string = String::from(val);
                    val_string.remove(0);
                    classes += &val_string;
                    classes += " ";
                } else if val.starts_with("#") {
                    if id_already_specified {
                        crate::errs::throw("Every element should have at most one id.");
                    }
                    id_already_specified = true;
                    let mut val_string = String::from(val);
                    val_string.remove(0);
                    attrs += &format!("id=\"{}\" ", val_string);
                } else {
                    crate::errs::throw(&format!("Unexpected identifier: {}", &val));
                }
            } else {
                attrs += val;
                attrs += " ";
            }
        }
        let classes_attr = if classes.len() > 0 {
            format!("class=\"{}\" ", classes)
        } else {
            String::new()
        };
        return classes_attr + &attrs;
    }
}
