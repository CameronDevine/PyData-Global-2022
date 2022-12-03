.PHONY: all

all: report.pdf

plot.png: plot.py data.csv
	python $^ $@

report.pdf: report.tex plot.png
	latexmk -pdf $<
