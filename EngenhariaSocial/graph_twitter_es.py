import twitter
import json
import nltk
import re
import networkx as nx

t = twitter.Twitter(domain='search.twitter.com')
resultados = []
#Grafico visual com RT por assuntos
g = nx.DiGraph()
for pagina in range(1,5):
    resultados.append( t.search(q='SNL', rpp=100, page=pagina) )

tweets = []
for resultado in resultados:
    for r in resultado['results']:
        tweets.append(r)

print 'tweets ' + str(len(tweets))

def origemRt(tweet):
    padrao = re.compile(r'(RT|via)(.@\w+)', re.IGNORECASE )
    return [origem.strip() for tupla in padrao.findall(tweet) for origem in tupla if origem not in ('RT', 'via') ]

for t in tweets:
    rt_origem = origemRt( t['text'] )
    if not rt_origem: continue
    for origem in rt_origem:
        g.add_edge (origem, t['from_user'], {'twitter_id' : t['id']})
      
print 'number_of_nodes'
print g.number_of_nodes()

print 'number_of_edges'
print g.number_of_edges()

print 'edges'
print g.edges(data=True)[0]

print 'len connected_components'
print len(nx.connected_components(g.to_undirected()))

print 'sorted degree'
print sorted(nx.degree(g))

OUT = 'search_results.dot'
try:
    nx.drawing.write_dot(g, OUT)
except ImportError, e:
    print e
dot = [ '"%s" -> "%s" [twitter_id=%s]' % (n1, n2, g[n1][n2]['twitter_id']) for n1, n2 in g.edges() ]
f = open(OUT, 'w')
f.write('strict digraph {\n%s\n}' % (';\n'.join(dot),))
f.close()

print 'Execute circo -Tpng -Osearch_results.dot search_results.dot'