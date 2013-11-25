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

	#print 'tabuleiro amostra'
	#for x in tabuleiro:
	#		print x

	for col in range(0,9):
		#print 'col: ' + str(col)
		for x in range(0,9):
			linhax = tabuleiro[x]
			#print 'linha x ' +str(linhax)
			for z in range (x,9):
				linhay = tabuleiro[z]
				#print 'linha y ' +str(linhay)
				if linhax != linhay:
					v1 = linhax[col]
					v2 = linhay[col]
					#print 'comparando v1:' +str(v1)+ ' v2:'+str(v2)
					if (v1 == v2 and v1 != 0):
						#print 'dados duplicados ' + str(v1) + ' ' +str(v2)
						#print 'x ' + str(linhax)
						#print 'y ' + str(linhay)
						return []
	return tabuleiro;
