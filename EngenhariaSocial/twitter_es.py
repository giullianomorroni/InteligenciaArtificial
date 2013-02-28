import twitter
import json
import nltk
import re

t = twitter.Twitter(domain='search.twitter.com')


#topicos mais falados
#t = twitter.Twitter(domain='search.twitter.com')
#resultados = t.trends()
#[r for r in resultados]


#busca por assunto paginado
#resultados = []
#for p in range(1,3):
# resultados.append(t.search(q='SNL', rpp=10, page=p))
#print json.dumps(resultados, sort_keys=True, indent=1) 


#Analise lexica das palavras
#resultados = []
#for p in range(1,3):
# resultados.append(t.search(q='SNL', rpp=10, page=p))
#
#tweets = []
#palavras = []
#
#for r in resultados:
#  tw = r['results'];
#  for t in tw:
#    tweets.append(t['text'])
#
#for t in tweets:
#  palavras += [p for p in t.split()]
#
#print 'total palavras ' + str(len(palavras))
#print 'total palavras unicas ' + str(len(set(palavras)))
#dl = 1.0 * len( set(palavras))/len(palavras) #diversidade lexica
#print 'diversidade lexica ' + str(dl)
#mediaPavavrasTweet = 1.0 * sum( [ len(t.split()) for t in tweets ] ) / len(tw)
#print 'media pavavras tweet ' + str(mediaPavavrasTweet)


#Analise de frequencia com NLTK
#resultados = t.search(q='SNL', rpp=50, page=1)
#tweets = []
#for r in resultados['results']:
#  tweets.append(r['text'])
#
#palavras = []
#for t in tweets:
#  palavras += [p for p in t.split()]
#
#frequencia = nltk.FreqDist(palavras)
#print 'Mais frequencia'
#print frequencia.keys()[:10]
#print 'Menos frequencia'
#print frequencia.keys()[-10:]


#Busca por RT
#padrao = re.compile(r'(RT|via)((?:\b\W*@\w+)+)', re.IGNORECASE )
padrao = re.compile(r'(RT|via)(.@\w+)', re.IGNORECASE )
#entra somente quem possui (RT OU via) E (@...)
exemplos = ['RT @giulliano funciona', 'funciona mesmo (via @giulliano)', 'esse nao (@giulliano)'] 
for e in exemplos:
    print padrao.findall(e)