use std::time::{Instant};

fn main() {
    let start = Instant::now();
    for i in 0..=10000 {
        // Do nothing, just loop
    }
    let duration = start.elapsed();
    println!("Rust Time: {:?}", duration);
}
