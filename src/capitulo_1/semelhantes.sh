#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Dados import Dados
from PessoaSemelhante import Semelhante

print 'Similiridade baseado em avaliacoes:'
d = Dados();
filmes = d.filmes();
s = Semelhante();
print s.semelhantes(filmes, "Giulliano");

print 'Similiridade baseado em itens em comum:'
item = 'Matrix'
print item;
itens = d.itens();
print s.semelhantes_por_item(itens, item);