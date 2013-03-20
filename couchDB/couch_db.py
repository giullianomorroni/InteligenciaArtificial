#! /usr/bin/python2.6

import httplib, json

def prettyPrint(s):
    '''
    Prettyprints the json response of an HTTPResponse object
    '''
    # HTTPResponse instance -> Python object -> str
    print json.dumps(json.loads(s.read()), sort_keys=True, indent=4)

'''
Basic wrapper class for operations on a couchDB
'''
class Couch:

    def __init__(self, host='localhost', port=5984, options=None):
        self.host = host
        self.port = port

    def connect(self):
        return httplib.HTTPConnection(self.host, self.port) # No close()

    '''
    Creates a new database on the server
    '''
    def createDb(self, dbName):
        r = self.put(''.join(['/',dbName,'/']), "")
        prettyPrint(r)

    '''
    Deletes the database on the server
    '''
    def deleteDb(self, dbName):
        r = self.delete(''.join(['/',dbName,'/']))
        prettyPrint(r)

    '''
    List the databases on the server
    '''
    def listDb(self):
        prettyPrint(self.get('/_all_dbs'))

    '''
    Returns info about the couchDB
    '''
    def infoDb(self, dbName):
        r = self.get(''.join(['/', dbName, '/']))
        prettyPrint(r)

    '''
    List all documents in a given database
    '''
    def listDoc(self, dbName):
        r = self.get(''.join(['/', dbName, '/', '_all_docs']))
        prettyPrint(r)

    '''
    Open a document in a given database
    '''
    def openDoc(self, dbName, docId):
        r = self.get(''.join(['/', dbName, '/', docId,]))
        prettyPrint(r)

    '''
    Save/create a document to/in a given database
    '''
    def saveDoc(self, dbName, body, docId=None):
        if docId:
            r = self.put(''.join(['/', dbName, '/', docId]), body)
        else:
            r = self.post(''.join(['/', dbName, '/']), body)
        prettyPrint(r)

    def deleteDoc(self, dbName, docId):
        # XXX Crashed if resource is non-existent; not so for DELETE on db. Bug?
        # XXX Does not work any more, on has to specify an revid
        #     Either do html head to get the recten revid or provide it as parameter
        r = self.delete(''.join(['/', dbName, '/', docId, '?revid=', rev_id]))
        prettyPrint(r)

    def get(self, uri):
        c = self.connect()
        headers = {"Accept": "application/json"}
        c.request("GET", uri, None, headers)
        return c.getresponse()

    def post(self, uri, body):
        c = self.connect()
        headers = {"Content-type": "application/json"}
        c.request('POST', uri, body, headers)
        return c.getresponse()

    def put(self, uri, body):
        c = self.connect()
        if len(body) > 0:
            headers = {"Content-type": "application/json"}
            c.request("PUT", uri, body, headers)
        else:
            c.request("PUT", uri, body)
        return c.getresponse()

    def delete(self, uri):
        c = self.connect()
        c.request("DELETE", uri)
        return c.getresponse()