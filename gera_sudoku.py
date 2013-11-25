#! /usr/bin/env python
#-*- coding: utf-8 -*-

import sudoku as sd

tabuleiro = sd.generate()
while len(tabuleiro) == 0:
	tabuleiro = sd.generate()
	if len(tabuleiro) > 0:
		print 'tabuleiro gerado'
		for x in tabuleiro:
			print x