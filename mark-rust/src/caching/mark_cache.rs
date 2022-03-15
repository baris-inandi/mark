extern crate base64;
use crate::utils::b64encode;

pub struct MarkCache {
    // The base64 encoded filename, used as the key in the cache.
    pub id: String,
}

impl MarkCache {
    pub fn new(path: &str) -> Self {
        return MarkCache {
            id: b64encode(path),
        };
    }
}
