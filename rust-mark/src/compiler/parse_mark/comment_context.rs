pub struct MarkCommentContext {
    pub comment_oneline: bool,   // //
    pub comment_multiline: bool, // /*  */
}

impl MarkCommentContext {
    pub fn new() -> MarkCommentContext {
        return MarkCommentContext {
            comment_oneline: false,
            comment_multiline: false,
        };
    }
}
