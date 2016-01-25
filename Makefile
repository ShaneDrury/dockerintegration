define HELP

This Makefile contains build and test commands for the dockerintegration project.

Usage:

make help          - Show this message
make clean         - Remove generated files
make test          - Run tests with coverage
endef

export HELP

.PHONY: help clean test

help:
	@echo "$$HELP"

clean:
	find . -name '*.pyc' -delete

test:
	py.test
