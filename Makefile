# Signifies our desired python version
# Makefile macros (or variables) are defined a little bit differently than traditional bash, keep in mind that in the Makefile there's top-level Makefile-only syntax, and everything else is bash script syntax.
PYTHON = python3
NAME = anaconda
FILE := requirements.txt

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo ---------------HELP-----------------
	@echo To setup the project type make setup
	@echo ------------------------------------

# Reads the requirements.txt and installs the packages
setup: requirements.txt
	pip3 install -r requirements.txt

# Run python script
run: 
	$(PYTHON) -m $(NAME)