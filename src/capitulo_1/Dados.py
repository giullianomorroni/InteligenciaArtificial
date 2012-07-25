# -*- coding: utf-8 -*-
'''
Created on 12/07/2012

@author: giulliano
'''
class Dados(object):
    
    def filmes(self):
        dados = {
            "Giulliano":    {"Matrix":4, "The God Father":3, "Sorte no Amor":1, "Sim Senhor":3, "Sexta-Feria 13":5},
            "Lucas":        {"Matrix":3.8, "The God Father":3, "Sorte no Amor":1, "Sim Senhor":3, "Sexta-Feria 13":4.6},
            "Pauline":      {"Matrix":2, "The God Father":1, "Sorte no Amor":3, "Sim Senhor":3, "Sexta-Feria 13":2},
            "Nelcina":      {"Matrix":1, "The God Father":1, "Sorte no Amor":4, "Sim Senhor":4, "Sexta-Feria 13":1},
            "Carlos":      {"Deus é Mais":1, "Documetario Gado":1, "Guerra Mortal":4, "Guerra Mortal 2":4, "Sexta-Feria 13":1}
            }
        return dados;
    
    def itens(self):
        dados = {
            "Matrix":           {"Giulliano", "Pauline", "Antonio", "Joao", "Maria", "Carlos", "Francisco", "Beatriz", "Carol"},
            "The God Father":   {"Giulliano", "Pauline", "Joao", "Carlos", "Francisco", "Beatriz", "Carol"},
            "Sorte no Amor":    {"Lucas", "Pauline", "Americo", "Jose", "Maria", "Carlos", "Francisco", "Fernanda"},
            "Sim Senhor":       {"Joel", "Manoel", "Antonio", "Maria", "Wanessa", "Carlos", "Francisco", "Claudio", "Carol"},
            }
        return dados;