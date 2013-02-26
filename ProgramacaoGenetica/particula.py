# -*- coding: utf-8 -*-

from Tvirus import comando
import decimal

class particula:
  global cromossomo;
  global totalComandos;
  global totalComandosSucedidos;

  def __init__(self, genetica):
    self.cromossomo = genetica;
    self.totalComandos = 0;
    self.totalComandosSucedidos = 0;

  def __str__(self):
    return str(self.cromossomo)

  def infectar(self):
    c = comando()
    for gene in self.cromossomo:
      if type(gene) is list:
	for subgene in gene:
	  func = getattr(c, subgene)
      else:
	func = getattr(c, gene)
      self.totalComandos += 1;
      resultadoComando = func()
      if (resultadoComando == True):
	self.totalComandosSucedidos += 1;

  def taxaSucesso(self):
    #print 'Total Comandos:' + str(self.totalComandos) + ' Comandos Sucedidos:' + str(self.totalComandosSucedidos)
    if (self.totalComandosSucedidos == 0):
      return 0;
    decimal.getcontext().prec = 2;
    return (decimal.Decimal(self.totalComandosSucedidos)/ decimal.Decimal(self.totalComandos)) * 100