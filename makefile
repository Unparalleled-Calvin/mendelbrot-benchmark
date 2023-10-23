# Makefile for compiling mandelbrot programs

# Compiler and compiler flags for each language
CXX = g++
GO = go build
JAVAC = javac
NODE = node
PYTHON = python3
RUSTC = rustc

BENCHMARK = benchmark.py

SOURCES = mandelbrot.cpp mandelbrot.go mandelbrot.java mandelbrot.js mandelbrot.py mandelbrot.rs mandelbrot.r

BINDIR = target

TARGETS = $(addprefix $(BINDIR)/, cpp_mandelbrot py_mandelbrot.py js_mandelbrot.js r_mandelbrot.r mandelbrot.class go_mandelbrot rust_mandelbrot)

all: $(TARGETS)

$(BINDIR)/cpp_mandelbrot: src/mandelbrot.cpp
	$(CXX) -o $@ $< -O3

$(BINDIR)/py_mandelbrot.py: src/mandelbrot.py
	cp $< $@

$(BINDIR)/js_mandelbrot.js: src/mandelbrot.js
	cp $< $@

$(BINDIR)/r_mandelbrot.r: src/mandelbrot.r
	cp $< $@

$(BINDIR)/mandelbrot.class: src/mandelbrot.java
	$(JAVAC) -d $(BINDIR) $< -O

$(BINDIR)/rust_mandelbrot: src/mandelbrot.rs
	$(RUSTC) -o $@ $< -Copt-level=3 -A warnings

$(BINDIR)/go_mandelbrot: src/mandelbrot.go
	$(GO) -o $@ $<

clean:
	rm -rf $(BINDIR)/*

# Ensure the bin directory exists
$(shell mkdir -p $(BINDIR))

.PHONY: all clean benchmark
