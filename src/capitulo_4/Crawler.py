'''
Created on 26/07/2012

@author: giulliano
'''

import urllib2
from BeautifulSoup import *
from urlparse import urljoin

class Crawler(object):

    ignorewords = set(['a','o','de','e', 'em']) 

    def __init__(self, dbname):
      self.con = sqllite.connect(dbname)

    def __del__(self):
        self.com.close();
    
    def dbcommit(self):
        self.com.commit();
    
    def getentryid(self, table, field, value, createnew=True):
        return None;
    
    def adtoindex(self, url, soup):
        if self.isindexed(url): return;
        print 'indexing %s', %url
        text = self.gettextonly(soup)
        words = self.separatewords(text)

    def gettextonly(self, soup):
        v = soup.string
        if v == None:
            c=soup.contents
        resulttext = ''
        for t in c:
          subtext = self.gettextonly(t)
          resulttext += subtext+'\n'
        return resulttext
      else:
        return v.strip()


    def separatewords(self, text):
        sppliter = re.compile('\\W*')
        return [s.lower() for s in sppliter(text) if s != '']

    def isindexed(self, url):
        return False;

    def addlinkref(self, urlfrom, utlto, linktext):
        pass;

    def crawl(self, pages, depth=2):
        for i in range(depth):
            newpages= set()
            for page in pages:
                try:
                    c = urllib2.urlopen(page);
                except:
                    print 'Could not open page %s' % page
                    continue
                soup = BeautifulSoup(c.read()) 
                self.addtoindex(page, soup)
                
                links = soup('a')
                for link in links:
                    if ('href' in dict(link.attrs)):
                        url=urljoin(page,link['href'])
                        if url.find('´') != -1: continue
                        url = url.split('#')[0]
                        if url[0:4] == 'http' and not self.isindexed(url):
                            newpages.add(url)
                        linktext = self.gettextonly(soup);
                        self.addlinkref(page, url, linktext)
                    self.dbcommit()
                pages = newpages

    def createindextables(self):
        self.con.execute('create table urllist (url)')
        self.con.execute('create table wordlist (word)')
        self.con.execute('create table wordlocation (urlid, wordid, location)')
        self.con.execute('create table link (fromid integer, toid integer)')
        self.con.execute('create table linkwords (wordid, linkid)')
        self.con.execute('create index wordidx on wordlist(word)')
        self.con.execute('create index urlidx on urllist(url)')
        self.con.execute('create index wordurlidx on wordlocation (wordid)')
        self.con.execute('create index urltoidx on link(toid)')
        self.con.execute('create index urlfromidx on link(fromid)')
