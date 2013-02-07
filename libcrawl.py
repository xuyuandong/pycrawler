#!/usr/bin/python
#encoding: utf-8

import sys
import re
import os
import urllib
import urllib2
import cookielib
import string
import time
import datetime
import fileinput
import httplib
import StringIO
import gzip
import socket

class Crawler(object):
  crawl_gap = 3
  myheaders = {
    "Accept":"image/gif, image/jpeg, image/pjpeg, image/pjpeg, application/x-shockwave-flash, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language":"zh-cn",
    "User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727)",
    "Referer": "http://www.baidu.com/",
    "Connection": "Keep-Alive",
    "Host": "www.baidu.com",
    "Cookie":"_HOP=; OVR=flt=0&flt2=0&flt3=0&flt4=0&flt5=0&flt6=0&flt7=0&flt8=0&flt9=0&flt10=0&flt11=0&flt12=0&ramp1=0&release=or3&preallocation=0&R=1; _SS=SID=C2885E5690964AD2AE6598C3B8DEAAA5&bIm=555&hIm=569&CW=1259&CH=630; MUID=6AABC8281DEF40A6AA27718C9A09A6A2; SRCHD=MS=1945975&SM=1&D=1945974&AF=NOFORM; SRCHUSR=AUTOREDIR=0&GEOVAR=&DOB=20110913; RMS=F=OgAgE&A=SAAAAAAAAAAQAAAg; _FS=ui=#en-US; _FP=mkt=en-US; SRCHUID=V=2&GUID=955CD7D73F9D412E949B33827AA8F32F"
}
  def __init__(self):
    urllib2.socket.setdefaulttimeout(10)

  def SetEngine(self, url, prefix):
    self.engine = url
    self.search = prefix

  def SetInterval(self, gap):
    self.crawl_gap = gap

  def Query(self, name, query, page_num = 1):
    # start
    conn=httplib.HTTPConnection(self.engine)
    # query
    url_data=urllib.urlencode(query)
    for k in range(0, page_num):
      # connect
      conn.request('GET', self.search + url_data, headers = self.myheaders)
      myresponse=conn.getresponse()
      print >>sys.stderr, "httpStaus:%d page:%d"%(myresponse.status, k+1)
      # decode
      compresseddata = myresponse.read()
      compressedstream = StringIO.StringIO(compresseddata)
      gzipper = gzip.GzipFile(fileobj = compressedstream)
      html = gzipper.read()
      # save
      fid_out = open(name + "_" + str(k) + ".htm", "w")
      fid_out.write(html)
      fid_out.close()
      # close      
      conn.close()
      # wait
      time.sleep(self.crawl_gap)


if __name__ == '__main__':
  crawler = Crawler()
  
  crawler.SetEngine("www.baidu.com", "/s?")
  data = {}
  data["rn"] = 100
  data["ie"] = 'utf-8'
  data["wd"] = "STL JAVA"

  # crawler.SetEngine("cn.bing.com", "/search?")
  # data = {}
  # data["q"] = "STL JAVA"

  # crawler.SetEngine("www.sogou.com", "/web?")
  # data = {}
  # data["num"] = 100
  # data["query"] = "STL JAVA"


  print >>sys.stderr,"Begin crawl baidu result!"
  crawler.Query("test", data)
  print >>sys.stderr,"Get baidu result OK!"


