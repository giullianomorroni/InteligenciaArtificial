#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Criticas import Criticas
from AnaliseEuclidiana import Euclidiana 

c = Criticas();
filmes = c.filmes();

a = Euclidiana();

similiridade = a.analise(filmes, "Giulliano", "Pauline");
print "Similaridade entre Giulliano e Pauline é de: " + str(similiridade);

similiridade = a.analise(filmes, "Giulliano", "Lucas");
print "Similaridade entre Giulliano e Lucas é de: " + str(similiridade);

similiridade = a.analise(filmes, "Pauline", "Nelcina");
print "Similaridade entre Pauline e Nelcina é de: " + str(similiridade);

similiridade = a.analise(filmes, "Giulliano", "Carlos");
print "Similaridade entre Giulliano e Carlos é de: " + str(similiridade);