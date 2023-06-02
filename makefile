PYTHON = python3
SCRIPT = main.py
ENV = myenv/bin/activate

all: run

run:
	source $(ENV) && \
	$(PYTHON) $(SCRIPT)
