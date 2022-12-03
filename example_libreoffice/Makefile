.PHONY: all

all: report.pdf

plot.png: plot.py data.csv
	python $^ $@

report.pdf: report.odt plot.png
	libreoffice --convert-to pdf $<
