'''
Created on 29/08/2012

@author: giulliano
'''

from galho import Galho

class ArvoreDecisao(object):

    def dados(self):
        d = [
        {'nome':'Angelica',       'idade':23,    'sexo':'f',    'estado':'casado',     'renda':'alta',      'escolaridade':'superior'},
        {'nome':'Monica',         'idade':45,    'sexo':'f',    'estado':'casado',     'renda':'alta',      'escolaridade':'colegial'},
        {'nome':'Giulliano',      'idade':32,    'sexo':'m',    'estado':'casado',     'renda':'media',     'escolaridade':'colegial'},
        {'nome':'Jose',           'idade':22,    'sexo':'m',    'estado':'casado',     'renda':'media',     'escolaridade':'colegial'},
        {'nome':'Carol',          'idade':45,    'sexo':'f',    'estado':'solteiro',   'renda':'baixa',     'escolaridade':'superior'},
        {'nome':'Carlos',         'idade':65,    'sexo':'m',    'estado':'viuvo',      'renda':'baixa',     'escolaridade':'superior'}]
        return d;
    
    def divisao(self, coluna, valor, valores=None):
        if valores == None:
            valores = self.dados()
        escolhidos = []
        outros = []
        #valores = self.dados()
        for v in valores:
            if v[coluna] == valor:
                escolhidos.append(v)
            else:
                outros.append(v) 
        d = []
        d.append(Galho().registrar(coluna, valor, 'Raiz', escolhidos))
        d.append(Galho().registrar('outros', valor, 'Raiz', outros))
        return d

    def segunda_divisao(self, coluna, valor, galho, pai):
        escolhidos = []
        outros = []

        for v in galho.valores:
            if v[coluna] == valor:
                escolhidos.append(v)
            else:
                outros.append(v) 
        d = []
        d.append(Galho().registrar(coluna, valor, pai, escolhidos))
        d.append(Galho().registrar('outros', valor, pai, outros))
        return d