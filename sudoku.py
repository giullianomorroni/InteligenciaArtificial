#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

linha1 = [0,2,3,0,5,0,7,8,9]
linha2 = [1,0,3,0,5,0,7,8,9]
linha3 = [1,2,0,4,5,0,7,8,0]
linha4 = [1,2,3,4,5,0,7,0,9]
linha5 = [1,2,0,4,5,6,7,8,9]
linha6 = [1,0,3,4,0,6,7,0,9]
linha7 = [1,2,0,4,5,6,7,8,0]
linha8 = [1,2,0,4,5,6,0,8,9]
linha9 = [1,0,3,4,0,6,0,8,9]

def verificarDuplicidadeVertical(linhax, linhay):
	for i in range(0,9):
		print linhax
		print linhay
		print ' '

		if linhax[i] == 0: return True;
		elif linhay[i] == 0: return True;

		if linhax[i] == linhay[i]:
			return False;
	return True;

def verificarDuplicidadeHorizontal(linhax):
	for x in range(0,9):
		for y in range(x+1,9):
			if linhax[x] == 0: return True;
			elif linhax[y] == 0: return True;

			if linhax[x] == linhax[y]:
				return False;
	return True;


def gerarTabuleiro():
	random.shuffle(linha1)
	random.shuffle(linha2)
	random.shuffle(linha3)
	random.shuffle(linha4)
	random.shuffle(linha5)
	random.shuffle(linha6)
	random.shuffle(linha7)
	random.shuffle(linha8)
	random.shuffle(linha9)
	tabuleiro = [ linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9 ]

	for x in range(0,9):
		if len(tabuleiro) == 0: break;
		for y in range(x+1,9):
			valido = (verificarDuplicidadeVertical(tabuleiro[x], tabuleiro[y]) and verificarDuplicidadeHorizontal(tabuleiro[y]) and verificarDuplicidadeHorizontal(tabuleiro[x]))
			print ('valido' + str(valido))
			if not valido:
				return []
				#break;#gerarTabuleiro(count+1)
	return tabuleiro

cont = 0;
while cont < 10000:
	cont=cont+1
	tabuleiro = gerarTabuleiro()
	print tabuleiro
	if len(tabuleiro) > 0:
		print 'tabuleiro gerado'
		for x in tabuleiro:
			print x
		break;
