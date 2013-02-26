# -*- coding: utf-8 -*-

import cPickle
from Tvirus import comando
from particula import particula

import cPickle
nova_populacao = cPickle.load(open('nova_populacao'))
for particula in nova_populacao:
  cromossomos = str(particula)
  print cromossomos
