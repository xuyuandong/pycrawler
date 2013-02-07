#!/usr/bin/env python
#encoding: utf-8
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, './BeautifulSoup'))

import BeautifulSoup

def parse(fname, out_file):
  a = open(fname)
  html = a.read()
  a.close()
  soup = BeautifulSoup.BeautifulSoup(html)
  #print soup.prettify()
  HT = soup.findAll('td', attrs={"class":"f"})
  
  fout = open(out_file, "w")
  for text in HT:
    print >>fout,text
    #fout.write(text + "\n")
  fout.close()

if __name__ == "__main__":
  fl = open(sys.argv[1])
  for line in fl:
    name = line.strip()
    name = name[name.find("/") + 1 :]
    name = name[: name.find(".")]
    out_name = "baidu_p/" + name + ".txt"
    parse(line.strip(), out_name)
  fl.close()
