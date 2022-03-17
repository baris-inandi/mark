pub fn is_cached(require_path: String) {
    /*
    TODO: import path module, join .cache with require path and check if exists, return file contents if exists, else error out
    */
    let f = match fs::read_to_string() {
        Ok(f) => f,
        Err(_) => crate::errs::throw("Could not read file, does it exist?"),
    };
}
