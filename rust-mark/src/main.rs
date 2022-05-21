// Copyright (C) 2022 baris-inandi
//
// This file is part of mark.
//
// mark is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 2 of the License, or
// (at your option) any later version.
//
// mark is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with mark.  If not, see <http://www.gnu.org/licenses/>.

use std::env;
pub mod compiler;
pub mod config;
pub mod errs;
pub mod require;
pub mod utils;

fn main() {
    config::load_config();
    let args: Vec<String> = env::args().collect();
    let out = compiler::parse_mark::parse(&format!("require {}", &args[1]), "<anonymous>");
    println!("{}", out);
}
