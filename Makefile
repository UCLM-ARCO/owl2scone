# -*- mode: makefile-gmake; coding: utf-8 -*-

SHELL   = /bin/bash
DIRNAME = $(notdir $(shell 'pwd'))
DESTDIR?=~

all:

install:
	install -d $(DESTDIR)/usr/bin/
	install -m 644 src/owl2scone.py $(DESTDIR)/usr/bin/owl2scone


PHONY: clean
clean:
	find . \( -name "*.pyc" -o -name "*~" \) -print -delete
