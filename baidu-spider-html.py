
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Evilys (evilys@foxmail.com)

 
import urllib
import urllib2
import re
import os

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
 



wb = raw_input("input your keyword:\n")  


class Spider:
 

    def __init__(self):
        self.siteURL = 'http://www.baidu.com/s?wd=' + wb

 

    def getPage(self,pageIndex):
        url = self.siteURL + "&pn=" + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')
 

    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="f13"><a target="_blank" href="(.*?)" class="c-showurl" style="text-.*?{"title":"(.*?)","url"',re.S)

        #none;">(.*?)&nbsp;.*?{"title":"(.*?)","url
        #<div class="f13"><a target="_blank" href="(.*?)" class="c-showurl" style="text-.*?{"title":"(.*?)","url"

        items = re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1]])
        return contents
 
    def savePageInfo(self,pageIndex):

        contents = self.getContents(pageIndex)
        for item in contents:
            
           y = open("results.html","a") 

           y.write('<a href="'+item[0]+'" target="_blank">'+'Title:'+item[1]+'</a>'+'<br>')




    def savePagesInfo(self,start):
        for i in  range(0,760,10):



            self.savePageInfo(i)
 


spider = Spider()
spider.savePagesInfo(0)


print '\n'"Everything is OK"