# -*- coding: utf-8 -*-
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

#adiciona valores a uma chave
r.sadd('pessoas', 'Giulliano Morroni', 'Pauline Santos')

#consulta os valores por chave
r.smembers('pessoas')

#total de elementos armazenados na chave
r.scard('pessoas')

#TRABALHANDO COM CONJUNTOS
r.sadd('Giulliano Morroni', 30, 'M', 'Solteiro')
r.sadd('Pauline Santos', 31, 'F', 'Solteiro')

#Retorna o que existe no primeiro que nao existe no segundo
r.sdiff('Giulliano Morroni', 'Pauline Santos')

#Retorna o que existe em todos
r.sinter('Giulliano Morroni', 'Pauline Santos')

#Retorna todos os valores de todos os conjuntos
r.sunion('Giulliano Morroni', 'Pauline Santos')



#Verifica se o valor faz parte do conjunto
r.sismember('Giulliano Morroni', 'F')

#Move o atributo 30 da origem para o destino
r.smove('Giulliano Morroni', 'Pauline Santos', 30)

#Retorna um valor aleatorio do conjunto
r.srandmember('Giulliano Morroni')
#Retorna X valores aleatorios do conjunto
r.srandmember('Giulliano Morroni',2)

#Remove um elemento
r.srem('Giulliano Morroni', 30)