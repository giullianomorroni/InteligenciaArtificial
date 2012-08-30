#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Crawler import Crawler
c = Crawler('searchindex.db')
#c.createindextables()
c.crawl(['http://giullianomorroni.com/portal'])
