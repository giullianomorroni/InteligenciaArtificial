#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Criticas import Criticas
from PessoaSemelhante import Semelhante

c = Criticas();
filmes = c.filmes();

s = Semelhante();

print s.semelhantes(filmes, "Giulliano");