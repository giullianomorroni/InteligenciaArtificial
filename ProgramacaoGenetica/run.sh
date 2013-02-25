#! /usr/bin/env python
#-*- coding: utf-8 -*-

#from Tvirus import comando
#c = comando()
#c.apagar()


#PASSO 1 - CRIAR A POPULAÇÃO INICIAL
'''
  ao importar este script serão geradas algumas variações do T-Virus
  as variações são salvas em um arquivo com o uso do cPickle
'''
import gerador_particulas

#PASSO 2 - EXECUTAR CICLO DE INFECÇÕES
import cPickle
variacoes = cPickle.load(open('variacoes'))
for v in variacoes:
  v.infectar()
  taxa = v.taxaSucesso()
  print (taxa)

#PASSO 3 - SEPARAR OS BEM SUCEDIDOS

