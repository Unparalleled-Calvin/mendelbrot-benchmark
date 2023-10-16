use std::ops::{Add, Mul};
use std::env;

#[derive(Copy, Clone)]
struct Complex {
    x: f64,
    y: f64,
}

impl Add for Complex {
    type Output = Self;
    fn add(self, other: Self) -> Self {
        Self {x: self.x + other.x, y: self.y + other.y}
    }
}

impl Mul for Complex {
    type Output = Self;
    fn mul(self, other: Self) -> Self{
        Self {x: self.x * other.x - self.y * other.y, y: self.x * other.y + self.y * other.x}
    }
}

fn abs(c: &Complex) -> f64 {
    c.x * c.x - c.y * c.y
}

fn linspace(vmin: f64, vmax: f64, length: i32) -> Vec<f64> {
    let step: f64 = (vmax - vmin) / (length - 1)  as f64;
    let mut ret: Vec<f64> = Vec::new();
    let mut i: i32 = 0;
    let mut v: f64 = vmin;
    while i < length {
        ret.push(v);
        i += 1;
        v += step;
    }
    ret
}

fn participants(X: &Vec<f64>, Y: &Vec<f64>) -> Vec<Complex> {
    let mut ret: Vec<Complex> = Vec::new();
    for &y in Y {
        for &x in X {
            ret.push(Complex { x: x, y: y })
        }
    }
    ret
}

fn calc(C: &Vec<Complex>, maxiter: i32, threshold: i32) -> Vec<i32> {
    let mut ret: Vec<i32> = Vec::new();
    for c in C {
        let mut z: Complex = Complex { x: 0.0, y: 0.0 };
        // let z_ref: &Complex = &z;
        let mut i: i32 = 0;
        while i < maxiter {
            z = z * z + *c;
            if abs(&z) > threshold as f64 {
                break;
            }
            i += 1;
        }
        ret.push(i);
    }
    ret
}

fn run(xmin: f64, xmax: f64, ymin: f64, ymax: f64, width: i32, height: i32, maxiter: i32) -> Vec<i32> {
    let threshold: i32 = 4;
    let X: Vec<f64> = linspace(xmin, xmax, width);
    let Y: Vec<f64> = linspace(ymin, ymax, height);
    let C: Vec<Complex> = participants(&X, &Y);
    let steps: Vec<i32> = calc(&C, maxiter, threshold);
    steps
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let xmin: f64 = args[1].parse().unwrap();
    let xmax: f64 = args[2].parse().unwrap();
    let ymin: f64 = args[3].parse().unwrap();
    let ymax: f64 = args[4].parse().unwrap();
    let width: i32 = args[5].parse().unwrap();
    let height: i32 = args[6].parse().unwrap();
    let maxiter: i32 = args[7].parse().unwrap();
    run(xmin, xmax, ymin, ymax, width, height, maxiter);
}