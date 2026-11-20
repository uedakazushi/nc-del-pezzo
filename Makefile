.PHONY: pdf verify clean
pdf:
	latexmk

verify:
	python3 computations/verify_formal_geometry.py
	python3 computations/verify_finite_families.py

clean:
	latexmk -C
