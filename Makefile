download: venv
	./venv/bin/python scripts/download.py

data/prtr-emissions.csv: venv download
	./venv/bin/python scripts/prtr-emissions.py

data/prtr-emissions.geojson: venv data/prtr-emissions.csv
	./venv/bin/python scripts/prtr-emissions-geojson.py

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

clean:
	rm -rf data/*.csv
	rm -rf data/*.geojson
	rm -rf files/*.csv

clean-venv:
	rm -rf venv

.PHONY: clean clean-venv download