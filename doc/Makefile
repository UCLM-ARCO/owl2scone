all: equivalents.pdf


equivalents.pdf : equivalents.tex
	pdflatex equivalents.tex
	pdflatex equivalents.tex

clean:
	$(RM) *~ *.aux *.log *.out *.pdf *.png
