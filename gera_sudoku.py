#! /usr/bin/env python
#-*- coding: utf-8 -*-

from bottle import route, run
from bottle import Bottle, request, response, run
from threading import Thread
import sudoku as sd

app = Bottle()

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/gera-sudoku', method=['OPTIONS', 'GET'])
def hello(source='ALL'):
	return str(generateSudoku(''))

def generateSudoku(threadName):
	print 'starting thread ' + threadName
	tabuleiro = sd.generate()
	count = 0
	while len(tabuleiro) == 0 and count < 10000:
		count = count+1
		tabuleiro = sd.generate()
		if len(tabuleiro) > 0:
			print 'tabuleiro gerado'
			print str(tabuleiro[0][0]) + ' ' + str(tabuleiro[1][0]) + ' ' + str(tabuleiro[2][0])
			print str(tabuleiro[0][1]) + ' ' + str(tabuleiro[1][1]) + ' ' + str(tabuleiro[2][1])
			print str(tabuleiro[0][2]) + ' ' + str(tabuleiro[1][2]) + ' ' + str(tabuleiro[2][2])

			print str(tabuleiro[3][0]) + ' ' + str(tabuleiro[4][0]) + ' ' + str(tabuleiro[5][0])
			print str(tabuleiro[3][1]) + ' ' + str(tabuleiro[4][1]) + ' ' + str(tabuleiro[5][1])
			print str(tabuleiro[3][2]) + ' ' + str(tabuleiro[4][2]) + ' ' + str(tabuleiro[5][2])

			print str(tabuleiro[6][0]) + ' ' + str(tabuleiro[7][0]) + ' ' + str(tabuleiro[8][0])
			print str(tabuleiro[6][1]) + ' ' + str(tabuleiro[7][1]) + ' ' + str(tabuleiro[8][1])
			print str(tabuleiro[6][2]) + ' ' + str(tabuleiro[7][2]) + ' ' + str(tabuleiro[8][2])
	print threadName + ' finished'
	return tabuleiro

'''
thread1 = Thread(target = generateSudoku, args = ('thread1',))
thread2 = Thread(target = generateSudoku, args = ('thread2',))
thread3 = Thread(target = generateSudoku, args = ('thread3',))
thread4 = Thread(target = generateSudoku, args = ('thread4',))
thread5 = Thread(target = generateSudoku, args = ('thread5',))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
'''

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost", help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=8880, help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))
