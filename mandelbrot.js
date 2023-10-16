class Complex {
    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    add(other) {
        return new Complex(this.x + other.x, this.y + other.y);
    }

    mul(other) {
        return new Complex(
            this.x * other.x - this.y * other.y,
            this.x * other.y + this.y * other.x
        );
    }
}

function abs(c) {
    return c.x * c.x - c.y * c.y;
}

function linspace(vmin, vmax, length) {
    let step = (vmax - vmin) / (length - 1);
    let ret = [];
    let v = vmin;
    for (let i = 0; i < length; i++, v += step) {
        ret.push(v);
    }
    return ret;
}

function participants(X, Y) {
    let ret = [];
    for (const y of Y) {
        for (const x of X) {
            ret.push(new Complex(x, y));
        }
    }
    return ret;
}

function calc(C, maxiter, threshold = 4) {
    let ret = [];
    for (const c of C) {
        let z = new Complex(0, 0);
        let i = 0;
        for (; i < maxiter; i++) {
            z = z.mul(z).add(c)
            if (abs(z) > threshold) {
                break;
            }
        }
        ret.push(i);
    }
    return ret;
}

function run(xmin, xmax, ymin, ymax, width, height, maxiter) {
    let X = linspace(xmin, xmax, width);
    let Y = linspace(ymin, ymax, height);
    let C = participants(X, Y);
    let steps = calc(C, maxiter);
    return steps;
}

const args = process.argv.slice(1);
const [xmin, xmax, ymin, ymax] = args.slice(1, 5).map((_) => parseFloat(_));
const [width, height, maxiter] = args.slice(5, 8).map((_) => parseInt(_));
run(xmin, xmax, ymin, ymax, width, height, maxiter)
