#! /usr/bin/env python
# -*- coding: utf-8 -*-

#from arvore_decisao import ArvoreDecisao
#a = ArvoreDecisao()
#v1 = a.divisao('sexo', 'm');
#v2 = a.nova_divisao('renda', 'alta', v1)
#a.imprimir(v2)

from arvore_decisao_2 import ArvoreDecisao
a = ArvoreDecisao()
v = a.divisao('sexo', 'm');
a.nova_divisao('renda', 'alta', v)
a.nova_divisao('escolaridade', 'colegial', v)
a.imprimir(v)