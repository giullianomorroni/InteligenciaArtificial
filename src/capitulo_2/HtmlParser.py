'''
Created on 24/07/2012

@author: giulliano
'''

from bs4 import BeautifulSoup

class HtmlParser(object):

    def read(self):
        soup = BeautifulSoup(open("index.html"))
        tag = soup.p;
        print tag;
        tagName = tag.name;
        print tagName;
        atributtes = tag.attrs;
        print atributtes;
        
    def read2(self):
        soup = BeautifulSoup(open("index.html"))
        tags = soup.find_all('a');
        print tags;
        link2 = tags[1];
        print link2.contents;
        
    def read3(self):
        soup = BeautifulSoup(open("index.html"))        
        for child in soup.descendants:
            print str(child).strip();
