use crate::utils::b64encode;
use std::fs;
use std::path::Path;
use std::time::SystemTime;

const CACHE_DIR: &str = "./.mark";

pub struct MarkCache {
    require_path: String,
    id: String,
    cache_file: String,
    meta_file: String,
}

impl MarkCache {
    pub fn new(require_path: String) -> std::io::Result<MarkCache> {
        // TODO: fix line below (doesn't work)
        Path::new(&CACHE_DIR);
        let id = b64encode(&require_path);
        let cache_file = Path::new(&CACHE_DIR).join(id.clone());
        let meta_file = Path::new(&CACHE_DIR).join(id.clone() + "_");
        if !cache_file.is_file() {
            fs::File::create(&cache_file)?;
        }
        if !meta_file.is_file() {
            fs::File::create(&meta_file)?;
        }
        return Ok(MarkCache {
            require_path,
            id,
            cache_file: cache_file.as_os_str().to_string_lossy().to_string(),
            meta_file: meta_file.as_os_str().to_string_lossy().to_string(),
        });
    }

    fn ensure(&self) {
        if !Path::new(&self.cache_file).is_file() {
            fs::File::create(&self.cache_file);
        }
        if !Path::new(&self.meta_file).is_file() {
            fs::File::create(&self.meta_file);
        }
    }

    pub fn update(&self, contents: String) {
        // write the newest modification time to the meta file
        self.ensure();
        fs::write(self.cache_file, contents);
    }

    pub fn get_if_cached(&self) -> std::io::Result<()> {
        self.ensure();
        let cached_modification_time = get_last_modification(self.id)?;
        let require_file_meta = fs::metadata(self.require_path)?.modified()?;
        let require_file_modification_time = system_time_as_string(&require_file_meta)?;

        println!(
            "{} {}",
            cached_modification_time, require_file_modification_time
        );
        return Ok(());
    }
}

fn system_time_as_string(t: &SystemTime) -> std::io::Result<String> {
    let duration = match t.duration_since(SystemTime::UNIX_EPOCH) {
        Ok(d) => d,
        Err(_) => {
            return Err(std::io::Error::new(
                std::io::ErrorKind::Other,
                "SystemTime Error",
            ))
        }
    };
    return Ok(duration.as_micros().to_string());
}

fn get_last_modification(cache_id: String) -> std::io::Result<String> {
    let cache_meta_file = Path::new(&CACHE_DIR).join(cache_id.clone() + "_");
    if !cache_meta_file.is_file() {
        fs::File::create(&cache_meta_file)?;
    }
    return Ok(fs::read_to_string(&cache_meta_file).unwrap());
}
