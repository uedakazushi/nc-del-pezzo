.PHONY: pdf verify clean
pdf:
	latexmk

verify:
	python3 computations/verify_surface_kuznetsov.py
	python3 computations/verify_formal_geometry.py
	python3 computations/verify_finite_families.py
	python3 computations/verify_cubic_top.py
	python3 computations/verify_elliptic_curve.py
	python3 computations/verify_degree_one_top.py
	python3 computations/verify_degree_one_curve.py
	python3 computations/verify_degree_one_center_jet.py
	python3 computations/verify_degree_two_gorenstein_curve.py
	python3 computations/verify_degree_one_integral_curve.py
	python3 computations/verify_poisson_shadow.py
	python3 computations/verify_degree_one_shadow_top.py
	python3 computations/verify_degree_two_shadow_top.py

clean:
	latexmk -C
