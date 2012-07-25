'''
Created on 12/07/2012

@author: giulliano
'''
from AnalisePearson import Pearson
import operator
from operator import itemgetter

class Semelhante(object):

    '''
    Define um semelhante da lista baseado nas avaliacoes feitas
    pelas pessoas contidas na lista.
    '''
    def semelhantes(self, prefs, nome):
        sm = {}
        p = Pearson();
        for pessoa in prefs:
            if (pessoa != nome):
                sm[pessoa] = p.analise(prefs, nome, pessoa);
                #deque.append()
                #a = str(pessoa) + str(p.analise(prefs, nome, pessoa))
                #sm.append(a); 

        lista = sorted(sm.iteritems(), key=operator.itemgetter(1))
        lista.reverse();
        return lista;
    
    '''
    Dado um item, busca por pessoas que o tenham e depois
    buscam os itens que eles compraram.
    '''
    def semelhantes_por_item(self, dados, filme):
        aux = [];
        #Todas as pessoas quem tem relacao com esse item
        pessoas = dados[filme];

        # Para cada item de uma lista, buscar outros itens que essas pessoas tem relacao
        for item in dados:
            for pessoa in dados[item]:
                if pessoa in pessoas:
                    tmp = dict(aux)
                    if tmp.has_key(item):
                        ttl = tmp.get(item)
                        aux.remove((item,tmp.get(item)))
                        aux.append((item,(ttl+1)))
                    else:
                        aux.append((item,1))

        #Remove o item atual
        sm = dict(aux);
        sm.pop(filme);
        #sm = sorted(sm, key=itemgetter(1))
        return sm;