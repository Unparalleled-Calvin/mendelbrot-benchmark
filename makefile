# Makefile for compiling mandelbrot programs

# Compiler and compiler flags for each language
CXX = g++
GO = go build
JAVAC = javac
NODE = node
PYTHON = python3
RUSTC = rustc

BENCHMARK = benchmark.py

SOURCES = mandelbrot.cpp mandelbrot.go mandelbrot.java mandelbrot.js mandelbrot.py mandelbrot.rs

BINDIR = target

TARGETS = $(addprefix $(BINDIR)/, cpp_mandelbrot py_mandelbrot.py js_mandelbrot.js java_mandelbrot.class go_mandelbrot rust_mandelbrot)

all: $(TARGETS)

$(BINDIR)/cpp_mandelbrot: src/mandelbrot.cpp
	$(CXX) -o $@ $<

$(BINDIR)/py_mandelbrot.py: src/mandelbrot.py
	cp $< $@

$(BINDIR)/js_mandelbrot.js: src/mandelbrot.js
	cp $< $@

$(BINDIR)/java_mandelbrot.class: src/mandelbrot.java
	$(JAVAC) -d $(BINDIR) $<

$(BINDIR)/rust_mandelbrot: src/mandelbrot.rs
	$(RUSTC) -o $@ $<

$(BINDIR)/go_mandelbrot: src/mandelbrot.go
	$(GO) -o $@ $<

benchmark:
	$(PYTHON) $(BENCHMARK)

clean:
	rm -rf $(BINDIR)/*

# Ensure the bin directory exists
$(shell mkdir -p $(BINDIR))

.PHONY: all clean benchmark
