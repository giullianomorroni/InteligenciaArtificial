# -*- coding: utf-8 -*-

from Tvirus import comando
from particula import particula

genetica = {};
c = comando();
ap = c.apagar();
cp = c.copiar();
at = c.atacar();
tr = c.transferir();
hp = c.hospedar();
pp = c.propagar();
ds = c.desligar();
ex = c.executar();
hb = c.hibernar();

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
    genetica[i] = (ex, ds, at, ap)
  elif (i == 5):
    genetica[i] = (pp, hp, hb)
  elif (i == 6):
    genetica[i] = (ap, cp, tr, pp)
  elif (i == 7):
    genetica[i] = (ds, tr, cp, [ap, ds])
  elif (i == 8):
    genetica[i] = (pp, ap, [cp, pp, at])
  elif (i == 9):
    genetica[i] = (ap, hb)
  elif (i == 10):
    genetica[i] = (ds)

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

print str([v for v in variacoes]);