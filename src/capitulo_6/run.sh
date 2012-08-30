#! /usr/bin/env python
# -*- coding: utf-8 -*-

from arvore_decisao import ArvoreDecisao 
a = ArvoreDecisao()
valores = a.divisao('idade', 65);
print 'Selecionados ' + str(valores[0])
print 'Outros ' + str(valores[1])
print '\n'

novos_valores = a.segunda_divisao('sexo', 'm', valores[0], valores[0].nome)
print '\n'
print 'Selecionados ' + str(novos_valores[0])
print 'Outros ' + str(novos_valores[1])

novos_valores = a.segunda_divisao('sexo', 'm', valores[1], valores[0].nome)
print '\n'
print 'Selecionados ' + str(novos_valores[0])
print 'Outros ' + str(novos_valores[1])

