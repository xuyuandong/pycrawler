#!/usr/bin/python
#encoding: utf-8

import sys
from libcrawl import Crawler

crawler = Crawler()
crawler.SetEngine("www.baidu.com", "/s?")
  
data = {}
data["rn"] = 100
data["ie"] = 'utf-8'

fin = open(sys.argv[1])

idx = 0
for line in fin:
  query = line.strip().split(' |')
  data["wd"] = query[0]
  idx += 1
  if idx <= 557:
    continue
  name = "baidu/" + str(idx)
  crawler.Query(name, data)
  print >>sys.stderr,"Get " + str(idx) + " query OK!"

fin.close()

