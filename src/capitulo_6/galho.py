'''
Created on 30/08/2012

@author: giulliano
'''

class Galho(object):

    global nome;
    global divisor;
    global pai;
    global valores;

    def registrar(self, nome, divisor, pai, valores):
        self.nome = nome;
        self.divisor = divisor
        self.pai = pai;
        self.valores = valores;
        return self

    def __str__(self):
        return ' -> Galho: ' + self.nome + ' Divisor:' + str(self.divisor) + ' Pai:' + str(self.pai) + ' Valores:' + str(self.valores)