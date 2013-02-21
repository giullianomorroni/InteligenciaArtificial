# -*- coding: utf-8 -*-

from Tvirus import comando

class particula:
  cromossomo = {};

  def __init__(self, genetica):
     self.cromossomo = genetica;

  def __str__(self):
    c = comando()
    resultado = ''
    for g in cromossomo:
      retorno += ' ' + g
    return resultado

  def infectar(self):
    c = comando()
    for g in cromossomo:
      func = getattr(c, g)
      func()