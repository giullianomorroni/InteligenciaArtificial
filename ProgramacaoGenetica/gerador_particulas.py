# -*- coding: utf-8 -*-

import cPickle
from Tvirus import comando
from particula import particula

genetica = {};
c = comando();
ap = 'apagar';
cp = 'copiar';
at = 'atacar';
tr = 'transferir';
hp = 'hospedar';
pp = 'propagar';
dl = 'desligar';
ex = 'executar';
hb = 'hibernar';

'''
Geração dos cromossomos
'''
for i in range(1,11):
  if (i == 1):
    genetica[i] = (ap, cp)
  elif (i == 2):
    genetica[i] = (cp, ap)
  elif (i == 3):
    genetica[i] = (at, hp, pp, ex)
  elif (i == 4):
    genetica[i] = (ex, dl, at, ap)
  elif (i == 5):
    genetica[i] = (pp, hp, hb)
  elif (i == 6):
    genetica[i] = (ap, cp, tr, pp)
  elif (i == 7):
    genetica[i] = (dl, tr, cp, [ap, dl])
  elif (i == 8):
    genetica[i] = (pp, ap, [cp, pp, at])
  elif (i == 9):
    genetica[i] = (ap, hb)
  elif (i == 10):
    genetica[i] = (dl, hb)

variacoes = []

'''
Criação das partículas
'''
for i in range(1,21):
  while (i >= 11):
    i = i - 3;
  while (i <= 0):
    i = i + 3;
  p = particula(genetica[i])
  variacoes.append(p)

print [str(v) for v in variacoes];

arq_variacoes = open('variacoes', 'w')
cPickle.dump(variacoes, arq_variacoes)
arq_variacoes.close()