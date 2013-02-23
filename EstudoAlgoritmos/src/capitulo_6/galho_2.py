'''
Created on 30/08/2012

@author: giulliano
'''

class Galho(object):

    nome = None
    divisor = None
    nivel = None
    valores = None
    pai = None

    def __init__(self, nome, divisor, nvl, pai=None):
        self.nivel = nvl
        self.nome = nome;
        self.divisor = divisor        
        self.valores = []
        self.pai = pai

    def registrarValores(self, valores):
        self.valores += valores;
        return self

    def __str__(self):
        if self.pai != None:
            return 'Galho: %s (%s) Nv: %s Pai %s' % (self.nome, str(self.divisor), str(self.nivel), str(self.pai.nome)) ;
        else:
            return 'Galho: %s (%s) Nv: %s ' % (self.nome, str(self.divisor), str(self.nivel)) ;

    def __cmp__(self, other):
        if other == None:
            return 1
        if self.nome == other.nome:
            return 0
        else:
            return 1