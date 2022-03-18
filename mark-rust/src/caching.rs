use crate::utils::b64encode;
use std::fs;
use std::path::Path;
use std::time::SystemTime;

const CACHE_DIR: &str = "./.mark";

pub struct MarkCache {
    require_path: String,
    cache_file: String,
    meta_file: String,
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
            cache_file: cache_file.as_os_str().to_string_lossy().to_string(),
            meta_file: meta_file.as_os_str().to_string_lossy().to_string(),
        });
    }

    fn ensure(&self) -> std::io::Result<()> {
        if !Path::new(&self.cache_file).is_file() {
            fs::File::create(&self.cache_file)?;
        }
        if !Path::new(&self.meta_file).is_file() {
            fs::File::create(&self.meta_file)?;
        }
        return Ok(());
    }

    pub fn update(&self, contents: &str) -> std::io::Result<()> {
        // write the newest modification time to the meta file
        self.ensure()?;
        fs::write(self.cache_file.clone(), contents)?;
        let file_metadata = fs::metadata(self.require_path.clone())?.modified()?;
        let file_modification_time = system_time_as_string(&file_metadata)?;
        fs::write(self.meta_file.clone(), file_modification_time)?;
        return Ok(());
    }

    pub fn get_if_cached(&self) -> std::io::Result<String> {
        self.ensure()?;
        let cached_modification = fs::read_to_string(self.meta_file.clone())?;
        let file_metadata = fs::metadata(self.require_path.clone())?.modified()?;
        let file_modification = system_time_as_string(&file_metadata)?;
        println!("{} {}", cached_modification, file_modification);
        if cached_modification == file_modification {
            return Ok(fs::read_to_string(&self.cache_file)?);
        } else {
            return Err(std::io::Error::new(std::io::ErrorKind::Other, "foo"));
        }
    }
}
