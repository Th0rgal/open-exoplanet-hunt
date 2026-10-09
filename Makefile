PYTHON ?= .venv/bin/python

.PHONY: verify test sync-catalogs vet-benchmark hunt

verify:
	$(PYTHON) -B scripts/verify_all.py

test:
	$(PYTHON) -B -m unittest discover -s tests -v

sync-catalogs:
	$(PYTHON) -B scripts/sync_catalogs.py

vet-benchmark:
	$(PYTHON) -B scripts/vet_candidate.py --tic 4206066 --period 3.182787 --secondary-period 11.1328 --status reference_benchmark_ddt100 --allow-benchmark

hunt:
	$(PYTHON) -B scripts/hunt_sectors.py --max-targets 10 --min-sectors 3
