#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

linha1 = [1,2,3,4,5,6,7,8,9]
linha2 = [1,2,3,4,5,6,7,8,9]
linha3 = [1,2,3,4,5,6,7,8,9]
linha4 = [1,2,3,4,5,6,7,8,9]
linha5 = [1,2,3,4,5,6,7,8,9]
linha6 = [1,2,3,4,5,6,7,8,9]
linha7 = [1,2,3,4,5,6,7,8,9]
linha8 = [1,2,3,4,5,6,7,8,9]
linha9 = [1,2,3,4,5,6,7,8,9]

tabuleiro = [ linha1, linha2, linha3, linha4, linha5, linha6, linha7, linha8, linha9 ]
valido = True

def verificarDuplicidadeVertical(linhax, linhay):
	for i in range(0,9):
		if linhax[i] == linhay[i]:
			return False;
	return True;

def verificarDuplicidadeHorizontal(linhax):
	for x in range(0,9):
		for y in range(x+1,9):
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

	for x in range(0,9):
		if len(tabuleiro) == 0: break;
		for y in range(x+1,9):
			valido = verificarDuplicidadeVertical(tabuleiro[x], tabuleiro[y]) and verificarDuplicidadeHorizontal(tabuleiro[y]) and verificarDuplicidadeHorizontal(tabuleiro[x])
			if not valido:
				del tabuleiro[0:]
				break;
				#break;#gerarTabuleiro(count+1)
cont = 0;
while cont < 10000:
	cont=cont+1
	gerarTabuleiro()
	if len(tabuleiro) > 0:
		print 'tabuleiro gerado'
		for x in tabuleiro:
			print x
