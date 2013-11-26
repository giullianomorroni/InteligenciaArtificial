#! /usr/bin/env python
#-*- coding: utf-8 -*-

import random

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

for s in sudoku:
	print ''
	for r in s:
		print r