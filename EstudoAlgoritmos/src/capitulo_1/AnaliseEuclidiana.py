'''
Created on 12/07/2012

@author: giulliano
'''
from math import sqrt

class Euclidiana(object):

    def analise(self, prefs, pessoa1, pessoa2):
        item_comum = 0;
        for item in prefs[pessoa1]:
            if item in prefs[pessoa2]:
                item_comum += 1
                break

        #Se nao tem itens em comum sai fora
        if item_comum == 0: return 0;

        soma_quadrados = sum([pow(prefs[pessoa1][item] - prefs[pessoa2][item], 2)
                              for item in prefs[pessoa1] if item in prefs[pessoa2]])

        #retorna entre 0 e 1
        #return 1 / (1+soma_quadrados);

        #soma-se 1 para evitar divisao por 0
        return 1 / (1+sqrt(soma_quadrados));