.PHONY: all

all: presentation.pdf

%.pdf: %.tex
	latexmk -pdf -shell-escape $<
