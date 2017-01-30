fn main() {
    let mut x = 0;
    for y in 0..55 {
        println!("20{}	{}", 16+y, x);
        x += "Ἕ䈯䘐".chars().nth(match y { 0...12 => 0, 13...18 => 1, _ => 2}).unwrap() as u32 + x as u32/118
    }
}
