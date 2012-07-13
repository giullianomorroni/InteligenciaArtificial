'''
Created on 12/07/2012

@author: giulliano
'''
from math import sqrt

class Pearson(object):

    def analise(self, prefs, pessoa1, pessoa2):
        item_comum = {};
        for item in prefs[pessoa1]:
            if item in prefs[pessoa2]:
                item_comum[item] = 1

        #Se nao tem itens em comum sai fora
        if len(item_comum) == 0: return 0;

        #Soma as preferencia
        soma1 = sum([prefs[pessoa1][item] for item in item_comum])
        soma2 = sum([prefs[pessoa2][item] for item in item_comum])

        #Soma o quadrado das preferencias
        qdrSoma1 = sum([pow(prefs[pessoa1][item],2) for item in item_comum])
        qdrSoma2 = sum([pow(prefs[pessoa2][item],2) for item in item_comum])
        
        #Soma os produtos
        somaProdutos = sum([prefs[pessoa1][item] * prefs[pessoa2][item] for item in item_comum])
        
        #Calcula a nota de Pearson
        num = somaProdutos -(soma1 * soma2 / len(item_comum)) 
        den = sqrt( (qdrSoma1-pow(soma1,2)/len(item_comum)) * (qdrSoma2-pow(soma2,2)/len(item_comum)) )
        
        if den == 0: return 0;
        return num/den;