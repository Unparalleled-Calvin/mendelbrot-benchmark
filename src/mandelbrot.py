import sys
from typing import List
import numpy as np

class Complex:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)
    
    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y,
                       self.x * other.y + self.y * other.x)

    def __abs__(self):
        return abs(self.x * self.x - self.y * self.y) #square of the actual mod

def linspace(vmin: float, vmax: float, length: int) -> List[float]:
    step = (vmax - vmin) / (length - 1)
    ret = []
    i = 0
    v = vmin
    while i < length:
        ret.append(v)
        v += step
        i += 1
    return ret

def participants(X: List[float], Y: List[float]) -> List[Complex]:
    ret = []
    for y in Y:
        for x in X:
            ret.append(Complex(x, y))
    return ret

def calc(C: List[Complex], maxiter: int, threshold: int = 4) -> List[int]:
    ret = []
    for c in C:
        z = Complex(0, 0)
        i = 0
        while i < maxiter:
            z = z * z + c
            if abs(z) > threshold:
                break
            i += 1
        ret.append(i)
    return ret

def run(xmin: float, xmax: float, ymin: float, ymax: float, width: int, height: int, maxiter: int):
    X = linspace(xmin, xmax, width)
    Y = linspace(ymin, ymax, height)
    C = participants(X, Y)
    steps = calc(C, maxiter)
    return steps

def plot(steps: List[int], width, height, filename = None):
    import numpy as np
    import matplotlib.pyplot as plt
    steps = np.array(steps)
    steps = steps.reshape((height, width))
    plt.imshow(steps, interpolation="nearest")
    if filename is not None:
        plt.savefig(filename)
    plt.show()

def test(
        xmin = -1,
        xmax = 1,
        ymin = -1,
        ymax = 1,
        width = 100,
        height = 100,
        maxiter = 124
    ):
    steps = run(xmin, xmax, ymin, ymax, width, height, maxiter)
    plot(steps, width, height, "test.jpg")

def mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter=20, threshold=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    A, B = np.meshgrid(x, y)
    C = A + B * 1j
    z = np.zeros_like(C)
    divtime = maxiter + np.zeros(z.shape, dtype=int)
    for i in range(maxiter):
        z = z ** 2 + C
        diverge = abs(z) > threshold  # who is diverging
        div_now = diverge & (divtime == maxiter)  # who is diverging now
        divtime[div_now] = i  # note when
        z[diverge] = threshold  # avoid diverging too much
    return divtime

if __name__ == "__main__":
    xmin, xmax, ymin, ymax = map(float, sys.argv[1:5])
    width, height, maxiter = map(int, sys.argv[5:8])
    mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter)
    # a = run(xmin, xmax, ymin, ymax, width, height, maxiter)