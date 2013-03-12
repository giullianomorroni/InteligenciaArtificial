#! /usr/bin/env python
#-*- coding: utf-8 -*-

from Tvirus import comando
import gerador_particulas
import cPickle

variacoes = cPickle.load(open('variacoes'))
nova_populacao = []
print '\nINICIANDO INFECÇÃO PARA POPULAÇÃO INICIAL DE PARTÍCULAS'
for v in variacoes:
  v.infectar()
  taxa = v.taxaSucesso()
  print 'TAXA DE SUCESSO ' + str(taxa) + '. PARTICULA ' + str(v) 
  if taxa >= 50:
    nova_populacao.append(v)

print '\nSELEÇÃO DOS MAIS FORTES CONCLUÍDA:'
for np in nova_populacao:
  print str(np)

arq = open('nova_populacao', 'w')
cPickle.dump(nova_populacao, arq)
arq.close()

import cruzamento_particulas

variacoes = cPickle.load(open('novas_variacoes'))
print '\nINICIANDO INFECÇÃO PARA SEGUNDA GERAÇÃO DE PARTÍCULAS'
for v in variacoes:
  v.infectar()
  taxa = v.taxaSucesso()
  print 'TAXA DE SUCESSO ' + str(taxa) + '. PARTICULA ' + str(v) 
  if taxa >= 50:
    nova_populacao.append(v)