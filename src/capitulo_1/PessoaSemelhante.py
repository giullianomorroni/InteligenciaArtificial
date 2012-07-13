'''
Created on 12/07/2012

@author: giulliano
'''
from AnalisePearson import Pearson
import operator

class Semelhante(object):

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