'''
Created on 29/08/2012

@author: giulliano
'''

from galho import Galho

class ArvoreDecisao(object):

    nvl = 1;

    def dados(self):
        d = [
        {'nome':'Angelica',       'idade':23,    'sexo':'f',    'estado':'casado',     'renda':'alta',      'escolaridade':'superior'},
        {'nome':'Monica',         'idade':45,    'sexo':'f',    'estado':'casado',     'renda':'alta',      'escolaridade':'colegial'},
        {'nome':'Giulliano',      'idade':32,    'sexo':'m',    'estado':'casado',     'renda':'media',     'escolaridade':'colegial'},
        {'nome':'Jose',           'idade':22,    'sexo':'m',    'estado':'casado',     'renda':'media',     'escolaridade':'colegial'},
        {'nome':'Carol',          'idade':45,    'sexo':'f',    'estado':'solteiro',   'renda':'baixa',     'escolaridade':'superior'},
        {'nome':'Gabriela',       'idade':65,    'sexo':'f',    'estado':'solteiro',   'renda':'media',     'escolaridade':'colegial'},
        {'nome':'Carlos',         'idade':65,    'sexo':'m',    'estado':'viuvo',      'renda':'baixa',     'escolaridade':'superior'}]
        return d;

    def divisao(self, coluna, valor, valores=None):
        if valores == None:
            valores = self.dados()
        escolhidos = []
        outros = []
        for v in valores:
            if v[coluna] == valor:
                escolhidos.append(v)
            else:
                outros.append(v) 
        d = []
        g1 = Galho(coluna, valor, self.nvl)
        g1.registrarValoresInteressantes(escolhidos)
        g1.registrarValoresNaoInteressantes(outros)
        d.append(g1)
        return d

    def nova_divisao(self, coluna, valor, galhos):
        self.nvl += 1
        for galho in galhos:
            valores = []
            if len(galho.filhos) > 0:
                valores = galho.filhos
            else:
                valores = galhos

            for filho in valores:
                escolhidos = []
                outros = []
                g1 = Galho(coluna, valor, self.nvl)
                valores = filho.interessa
                for v in valores:
                    if v[coluna] == valor:
                        escolhidos.append(v)
                    else:
                        outros.append(v)
                g1.registrarValoresInteressantes(escolhidos)
                g1.registrarValoresNaoInteressantes(outros)
                galho.adicionarFilho(g1)

        for galho in galhos:
            valores = []
            if len(galho.filhos) > 0:
                valores = galho.filhos
            else:
                valores = galhos

            for filho in valores:
                escolhidos = []
                outros = []
                g1 = Galho(coluna, valor, self.nvl)
                valores = filho.n_interessa
                for v in valores:
                    if v[coluna] == valor:
                        escolhidos.append(v)
                    else:
                        outros.append(v)
                g1.registrarValoresInteressantes(escolhidos)
                g1.registrarValoresNaoInteressantes(outros)
                galho.adicionarFilho(g1)                
        return galhos

    def imprimir(self, galhos):
        self.imprimirGalho(galhos, (1))

    def imprimirGalho(self, galhos, line):
        print str(galhos[line-1])
        for galho in galhos:
            print '    Interessa:'
            for v in galho.interessa:
                print '        ' + str(v)
            print '    Nao Interessa:'
            for v in galho.n_interessa:
                print  '        ' + str(v)
            if len(galho.filhos) > 0:
                print str(galho.filhos[line-1])
            for filho in galho.filhos:
                print '    Interessa:'
                for v in filho.interessa:
                    print '        ' + str(v)
                print '    Nao Interessa:'
                for v in filho.n_interessa:
                    print  '        ' + str(v)
