INSTALL_SCRIPT = install.sh
PYTHON_SCRIPT = main.py

all: install run

install:
	@echo "Running install.sh to install dependencies..."
	@chmod +x $(INSTALL_SCRIPT)
	@./$(INSTALL_SCRIPT)

run:
	@echo "Running main.py..."
	@python3 $(PYTHON_SCRIPT)

clean:
	@echo "Cleaning temporary files..."

help:
	@echo "Makefile for running IP-LOC By Wanz Xploit tool"
	@echo "Available targets:"
	@echo "  all       : Install dependencies and run main.py"
	@echo "  install   : Install dependencies using install.sh"
	@echo "  run       : Run main.py"
	@echo "  clean     : Clean temporary files (if any)"
	@echo "  help      : Display this information"