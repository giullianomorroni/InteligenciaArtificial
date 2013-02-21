#! /usr/bin/env python
# -*- coding: utf-8 -*-

from arvore_decisao import ArvoreDecisao
 
a = ArvoreDecisao()

v1 = a.divisao('sexo', 'm');

#v2 = a.nova_divisao('sexo', 'm', v1)

v2 = a.nova_divisao('renda', 'alta', v1)

a.imprimir(v2)
