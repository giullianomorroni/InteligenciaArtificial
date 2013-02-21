'''
Created on 30/08/2012

@author: giulliano
'''

class Galho(object):

    nome = None
    divisor = None
    filhos = None
    nivel = None

    interessa = None
    n_interessa = None

    def __init__(self, nome, divisor, nvl):
        self.nivel = nvl
        self.nome = nome;
        self.divisor = divisor        
        self.filhos = [];
        self.interessa = []
        self.n_interessa = []

    def registrarValoresInteressantes(self, valores):
        self.interessa += valores;
        return self

    def registrarValoresNaoInteressantes(self, valores):
        self.n_interessa += valores;
        return self

    def adicionarFilho(self, filho):
        if (filho in self.filhos):
            f = self.filhos.pop( self.filhos.index(filho) )
            f.n_interessa += filho.n_interessa
            f.interessa  += filho.interessa
            self.filhos.append(f)
        else:
            self.filhos.append(filho)

    def __str__(self):
        return 'Galho: %s (%s) Nv: %s' % (self.nome, str(self.divisor), str(self.nivel)) ;

    def __cmp__(self, other):
        if self.nome == other.nome:
            return 0
        else:
            return 1