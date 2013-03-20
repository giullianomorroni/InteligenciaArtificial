def test():
    foo = Couch('localhost', '5984')

    print '\nCreate database 'mydb':'
    foo.createDb('mydb')

    print '\nList databases on server:'
    foo.listDb()

    print '\nCreate a document 'mydoc' in database 'mydb':'
    doc = '''
    {
        'value':
        {
            'Subject':'I like Planktion',
            'Author':'Rusty',
            'PostedDate':'2006-08-15T17:30:12-04:00',
            'Tags':['plankton', 'baseball', 'decisions'],
            'Body':'I decided today that I don't like baseball. I like plankton.'
        }
    }
    '''
    foo.saveDoc('mydb', doc, 'mydoc')

    print '\nCreate a document, using an assigned docId:'
    foo.saveDoc('mydb', doc)

    print '\nList all documents in database 'mydb''
    foo.listDoc('mydb')

    print '\nRetrieve document 'mydoc' in database 'mydb':'
    foo.openDoc('mydb', 'mydoc')

    print '\nDelete document 'mydoc' in database 'mydb':'
    foo.deleteDoc('mydb', 'mydoc')

    print '\nList all documents in database 'mydb''
    foo.listDoc('mydb')

    print '\nList info about database 'mydb':'
    foo.infoDb('mydb')

    print '\nDelete database 'mydb':'
    foo.deleteDb('mydb')

    print '\nList databases on server:'
    foo.listDb()

if __name__ == '__main__':
    test()