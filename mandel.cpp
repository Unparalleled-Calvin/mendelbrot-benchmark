#include <vector>

class Complex {
public:
    double x, y;
    Complex(double x = 0, double y = 0);
    friend Complex operator+(const Complex& c1, const Complex& c2);
    friend Complex operator*(const Complex& c1, const Complex& c2);
    friend double abs(const Complex& c);
};

Complex::Complex(double x, double y) : x(x), y(y) {}

Complex operator+(const Complex& c1, const Complex& c2) {
    return Complex(c1.x + c2.x, c1.y + c2.y);
}

Complex operator*(const Complex& c1, const Complex& c2) {
    return Complex(c1.x * c2.x - c1.y * c2.y, c1.x * c2.y + c1.y * c2.x);
}

double abs(const Complex& c) {
    return c.x * c.x - c.y * c.y;
}

std::vector<double> linspace(double vmin, double vmax, int length) {
    double step = (vmax - vmin) / (length - 1);
    std::vector<double> ret;
    int i = 0;
    double v = vmin;
    for (; i < length; i++, v += step) {
        ret.emplace_back(v);
    }
    return ret;
}

std::vector<Complex> participants(const std::vector<double>& X, const std::vector<double>& Y) {
    std::vector<Complex> ret;
    for (double y : Y) {
        for (double x : X) {
            ret.emplace_back(x, y);
        }
    }
    return ret;
}


std::vector<int> calc(const std::vector<Complex>& C, int maxiter, int threshold = 4) {
    std::vector<int> ret;
    for (const Complex& c : C) {
        Complex z(0, 0);
        int i = 0;
        for (;i < maxiter;i++) {
            z = z * z + c;
            if (abs(z) > threshold) {
                break;
            }
        }
        ret.emplace_back(i);
    }
    return ret;
}

std::vector<int> run(double xmin, double xmax, double ymin, double ymax, int width, int height, int maxiter) {
    std::vector<double> X = linspace(xmin, xmax, width);
    std::vector<double> Y = linspace(ymin, ymax, height);
    std::vector<Complex> C = participants(X, Y);
    std::vector<int> steps = calc(C, maxiter);
    return steps;
}