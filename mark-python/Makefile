shell:
	poetry shell

run:
	python ./mark/__main__.py compile ../ignore/main.mark

run-watch:
	python ./mark/__main__.py watch ../ignore/main.mark

install:
	sudo pex . -v -e mark -o /usr/bin/mark

build:
	pex . -v -e mark -o build.pex
