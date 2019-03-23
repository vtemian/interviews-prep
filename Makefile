PROBLEMS := $(shell find cracking-the-code-interview/ -name *.py)
TESTS_PROBLEMS := $(addprefix test-, $(PROBLEMS))

.PHONY: tests
tests: $(TESTS_PROBLEMS)
	@echo $^

.PHONY: tests-cracking
test-cracking-the-code-interview/%:
	python3 cracking-the-code-interview/$*
