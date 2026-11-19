.PHONY: pdf verify clean
pdf:
	latexmk

verify:
	python3 computations/verify_formal_geometry.py

clean:
	latexmk -C
