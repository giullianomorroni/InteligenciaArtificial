#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

def is_duplicated(contador):
	duplicated = False
	#print ' '
	for d in range(1,9): 
		#print str(d) + ' ' + str(contador.count(d))
		if contador.count(d) > 1:
			duplicated = True
			#print ' duplicados ' + str(contador)
			return duplicated
	return duplicated

def generate():
	sudoku = []

	for i in range(9):
		numbers = [1,2,3,4,5,6,7,8,9]
		random.shuffle(numbers)

		row = []
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())
		row.append(numbers.pop())

		square = [[],[],[]]

		square[0] = row[0:3]
		square[1] = row[3:6]
		square[2] = row[6:9]

		sudoku.append(square)

	#easy mode
	for i in range(1,100):
		remove_on = random.randint(1,2)
		if remove_on == 2:
			#print sudoku[random.randint(0,8)][random.randint(0,2)][random.randint(0,2)]
			sudoku[random.randint(0,8)][random.randint(0,2)][random.randint(0,2)] = 0

	# Analise na vertical
	for coluna in range(0,3):
		contador = []
		contador.append(sudoku[0][0][coluna])
		contador.append(sudoku[0][1][coluna])
		contador.append(sudoku[0][2][coluna])

		contador.append(sudoku[3][0][coluna])
		contador.append(sudoku[3][1][coluna])
		contador.append(sudoku[3][2][coluna])

		contador.append(sudoku[6][0][coluna])
		contador.append(sudoku[6][1][coluna])
		contador.append(sudoku[6][2][coluna])
		if is_duplicated(contador): return []

	for coluna in range(0,3):
		contador = []
		contador.append(sudoku[1][0][coluna])
		contador.append(sudoku[1][1][coluna])
		contador.append(sudoku[1][2][coluna])

		contador.append(sudoku[4][0][coluna])
		contador.append(sudoku[4][1][coluna])
		contador.append(sudoku[4][2][coluna])

		contador.append(sudoku[7][0][coluna])
		contador.append(sudoku[7][1][coluna])
		contador.append(sudoku[7][2][coluna])
		if is_duplicated(contador): return []

	for coluna in range(0,3):
		contador = []
		contador.append(sudoku[2][0][coluna])
		contador.append(sudoku[2][1][coluna])
		contador.append(sudoku[2][2][coluna])

		contador.append(sudoku[5][0][coluna])
		contador.append(sudoku[5][1][coluna])
		contador.append(sudoku[5][2][coluna])

		contador.append(sudoku[8][0][coluna])
		contador.append(sudoku[8][1][coluna])
		contador.append(sudoku[8][2][coluna])
		if is_duplicated(contador): return []


	# Analise na horizontal
	for coluna in range(0,3):
		contador = []
		contador.append(sudoku[0][coluna][0])
		contador.append(sudoku[0][coluna][1])
		contador.append(sudoku[0][coluna][2])

		contador.append(sudoku[1][coluna][0])
		contador.append(sudoku[1][coluna][1])
		contador.append(sudoku[1][coluna][2])

		contador.append(sudoku[2][coluna][0])
		contador.append(sudoku[2][coluna][1])
		contador.append(sudoku[2][coluna][2])
		if is_duplicated(contador): return []

	for coluna in range(0,3):
		contador = []
		contador.append(sudoku[3][coluna][0])
		contador.append(sudoku[3][coluna][1])
		contador.append(sudoku[3][coluna][2])

		contador.append(sudoku[4][coluna][0])
		contador.append(sudoku[4][coluna][1])
		contador.append(sudoku[4][coluna][2])

		contador.append(sudoku[5][coluna][0])
		contador.append(sudoku[5][coluna][1])
		contador.append(sudoku[5][coluna][2])
		if is_duplicated(contador): return []

	for coluna in range(0,3):
		contador = []
		contador.append(sudoku[6][coluna][0])
		contador.append(sudoku[6][coluna][1])
		contador.append(sudoku[6][coluna][2])

		contador.append(sudoku[7][coluna][0])
		contador.append(sudoku[7][coluna][1])
		contador.append(sudoku[7][coluna][2])

		contador.append(sudoku[8][coluna][0])
		contador.append(sudoku[8][coluna][1])
		contador.append(sudoku[8][coluna][2])
		if is_duplicated(contador): return []
		
	return sudoku