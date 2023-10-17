package main

import (
	"math"
	"strconv"
	"os"
)

type Complex struct {
	x, y float64
}

func NewComplex(x, y float64) Complex {
	return Complex{x, y}
}

func (c Complex) Add(other Complex) Complex {
	return Complex{c.x + other.x, c.y + other.y}
}

func (c Complex) Mul(other Complex) Complex {
	return Complex{c.x * other.x - c.y * other.y, c.x * other.y + c.y * other.x}
}

func (c Complex) Abs() float64 {
	return math.Abs(c.x * c.x - c.y * c.y)
}

func linspace(vmin, vmax float64, length int) []float64 {
	step := (vmax - vmin) / float64(length-1)
	ret := make([]float64, 0)
	v := vmin
	for i := 0; i < length; i++ {
		ret = append(ret, v)
		v += step
	}
	return ret
}

func participants(X, Y []float64) []Complex {
	ret := make([]Complex, 0)
	for _, y := range Y {
		for _, x := range X {
			ret = append(ret, Complex{x, y})
		}
	}
	return ret
}

func calc(C []Complex, maxiter int, threshold int) []int {
	ret := make([]int, 0)
	for _, c := range C {
		z := NewComplex(0, 0)
		i := 0
		for ; i < maxiter; i++ {
			z = z.Mul(z).Add(c)
			if z.Abs() > float64(threshold) {
				break
			}
		}
		ret = append(ret, i)
	}
	return ret
}

func run(xmin, xmax, ymin, ymax float64, width, height, maxiter int) []int {
	X := linspace(xmin, xmax, width)
	Y := linspace(ymin, ymax, height)
	C := participants(X, Y)
	steps := calc(C, maxiter, 4)
	return steps
}

func main() {
    xmin, _ := strconv.ParseFloat(os.Args[1], 64)
	xmax, _ := strconv.ParseFloat(os.Args[2], 64)
	ymin, _ := strconv.ParseFloat(os.Args[3], 64)
	ymax, _ := strconv.ParseFloat(os.Args[4], 64)
	width, _ := strconv.Atoi(os.Args[5])
	height, _ := strconv.Atoi(os.Args[6])
	maxiter, _ := strconv.Atoi(os.Args[7])

	run(xmin, xmax, ymin, ymax, width, height, maxiter)
}
