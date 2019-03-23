.PHONY: tests
tests: tests-cracking

.PHONY: tests-cracking
tests-cracking:
	for f in $(find cracking-the-code-interview/ -name "*.py"); do python $f; done
