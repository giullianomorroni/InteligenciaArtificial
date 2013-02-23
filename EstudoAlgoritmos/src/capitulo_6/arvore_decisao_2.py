'''
Created on 29/08/2012

@author: giulliano
'''

from galho_2 import Galho

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
        g1.registrarValores(escolhidos)
        d.append(g1)
        g2 = Galho('!'+coluna, valor, self.nvl)
        g2.registrarValores(outros)
        d.append(g2)
        return d

    def nova_divisao(self, coluna, valor, galhos):
        self.nvl += 1
        aux = []
        for galho in galhos:
            escolhidos = []
            outros = []
            for v in galho.valores:
                if v[coluna] == valor:
                    escolhidos.append(v)
                else:
                    outros.append(v)
            g1 = Galho(coluna, valor, self.nvl, galho)
            g1.registrarValores(escolhidos)
            g2 = Galho('!'+coluna, valor, self.nvl, galho)
            g2.registrarValores(outros)
            aux.append(g1)
            aux.append(g2)
        galhos += aux
        print len(galhos)

    def imprimir(self, galhos):
        impressos = []

        for galho in galhos:
            if galho in impressos:
                continue
            print galho
            impressos.append(galho)
            for v in galho.valores:
                print '    ' + str(v)

            for galho2 in galhos:
                if galho2.pai == galho:
                    print '    ' + str(galho2)
                    impressos.append(galho2)
                    for v in galho2.valores:
                        print '        ' + str(v)

                    for galho3 in galhos:
                        if galho3.pai == galho2:
                            print '        ' + str(galho3)
                            impressos.append(galho3)
                            for v in galho3.valores:
                                print '            ' + str(v)