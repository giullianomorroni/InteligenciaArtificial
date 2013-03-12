# -*- coding: utf-8 -*-

import cPickle
from Tvirus import comando
from particula import particula

genetica = {};
c = comando();

print '\nCRIANDO MAPAS GENÉTICOS ALEATORIAMENTE:'
for i in range(1,11):
  genetica[i] = c.mutacao()

print str(genetica)

'''
Criação das partículas (populacao)
'''
print '\nCRIANDO PARTÍCULAS COM BASE NAS GENÉTICAS DISPONÍVEIS:'
variacoes = []
for i in range(1,21):
  while (i >= 11):
    i = i - 3;
  while (i <= 0):
    i = i + 3;
  p = particula('P'+str(i), genetica[i])
  variacoes.append(p)

for v in variacoes:
  print str(v)

arq_variacoes = open('variacoes', 'w')
cPickle.dump(variacoes, arq_variacoes)
arq_variacoes.close()