#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

linha1 = [0,2,3,0,5,0,7,8,9]
linha2 = [1,0,3,0,5,0,7,0,0]
linha3 = [1,2,0,4,5,0,7,8,0]
linha4 = [1,2,0,4,5,0,7,0,9]
linha5 = [1,2,0,4,0,6,0,8,9]
linha6 = [0,0,3,4,0,0,7,0,9]
linha7 = [1,2,0,4,5,6,7,8,0]
linha8 = [0,2,0,0,5,6,0,8,9]
linha9 = [1,0,3,0,0,6,0,8,9]

def generate():
	random.shuffle(linha1)
	random.shuffle(linha4)
	random.shuffle(linha8)
	random.shuffle(linha3)
	random.shuffle(linha5)
	random.shuffle(linha7)
	random.shuffle(linha6)
	random.shuffle(linha9)
	random.shuffle(linha2)
	tabuleiro = [ linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9 ]
	#print tabuleiro
	return tabuleiro

tabuleiro = []
valido = False

def go():
	tabuleiro = generate()
	for x in range(8):
		linhax = tabuleiro[x]
		for z in range (9):
			if len(tabuleiro) > z+1:
				linhay = tabuleiro[z+1]
				if (linhax != linhay):
					v1 = linhax[z]
					v2 = linhay[z]
					if (v1 == v2 and v1 != 0):
						print 'dados duplicados ' + str(v1) + ' ' +str(v2)
						print 'x ' + str(linhax)
						print 'y ' + str(linhay)
						return go()
				else:
					return go()
			if x == 8 and z == 8: return tabuleiro;
tabuleiro = go()
print 'tabuleiro gerado'
for x in tabuleiro:
	print x
