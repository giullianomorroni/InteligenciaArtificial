# -*- coding: utf-8 -*-

import cPickle
from Tvirus import comando
from particula import particula

import cPickle

variacoes = [];

nova_populacao = cPickle.load(open('nova_populacao'))
#for particula in nova_populacao:
#  cromossomos = str(particula)
#  print cromossomos

'''
Mutação (cruzamento) das melhores partículas 
'''
while (len(nova_populacao) >= 2):
  p1 = nova_populacao.pop()
  p2 = nova_populacao.pop()

  variacao = []
  for v in p1.genetica():
    variacao.append(v)
  for v in p2.genetica():
    variacao.append(v)

  print variacao

  p = particula( variacao )
  variacoes.append(p)

arq_variacoes = open('novas_variacoes', 'w')
cPickle.dump(variacoes, arq_variacoes)
arq_variacoes.close()