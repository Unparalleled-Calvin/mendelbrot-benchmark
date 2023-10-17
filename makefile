# Makefile for compiling mandelbrot programs

# Compiler and compiler flags for each language
CXX = g++
GO = go build
JAVAC = javac
NODE = node
PYTHON = python3
RUSTC = rustc

# Source files
SOURCES = mandelbrot.cpp mandelbrot.go mandelbrot.java mandelbrot.js mandelbrot.py mandelbrot.rs

# Binaries directory
BINDIR = target

# Targets for each source file
TARGETS = $(addprefix $(BINDIR)/, cpp_mandelbrot py_mandelbrot.py js_mandelbrot.js java_mandelbrot.class go_mandelbrot rust_mandelbrot)

# Default target
all: $(TARGETS)

# Rule to compile C++ source with language prefix
$(BINDIR)/cpp_%: src/%.cpp
	$(CXX) -o $@ $<

# Rule to run Python source with language prefix
$(BINDIR)/py_%: src/%
	cp $< $@

# Rule to run JavaScript source with language prefix
$(BINDIR)/js_%: src/%
	cp $< $@

# Rule to compile Java source with language prefix
$(BINDIR)/java_%.class: src/%.java
	$(JAVAC) -d $(BINDIR) $<

# Rule to compile Rust source with language prefix
$(BINDIR)/rust_%: src/%.rs
	$(RUSTC) -o $@ $<

# Rule to compile Go source with language prefix
$(BINDIR)/go_%: src/%.go
	$(GO) -o $@ $<

# Clean up generated files
clean:
	rm -rf $(BINDIR)/*

# Ensure the bin directory exists
$(shell mkdir -p $(BINDIR))

.PHONY: all clean
