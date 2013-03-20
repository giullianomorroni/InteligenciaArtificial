import couchdb

couch = couchdb.Server() # Assuming localhost:5984
#couch = couchdb.Server('http://localhost:5984/')

# select database
db = couch['hell_world']

#create a document and insert it into the db:
doc = {'foo': 'bar'}
db.save(doc)