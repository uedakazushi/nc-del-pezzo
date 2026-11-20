.PHONY: pdf verify clean
pdf:
	latexmk

verify:
	python3 computations/verify_formal_geometry.py
	python3 computations/verify_finite_families.py
	python3 computations/verify_cubic_top.py
	python3 computations/verify_elliptic_curve.py

clean:
	latexmk -C
