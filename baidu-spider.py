#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-1-24 20:34:30
# @Author  : Evilys (evilys@foxmail.com)



import urllib

import urllib2

import re



print '''

                   Baidu Spiders V1.0



     1.  The value must be in multiples of 10!  





'''



wb = "site:.jmpt.cn"  #这里输入你的关键词/Input your keywords here

Pagenumber = raw_input("input your value:\n")  #必须是10的倍数







class BadiuSpider:



    def __init__(self):





        self.URL = 'http://www.baidu.com/s?wd=' + wb + '&pn=' + Pagenumber 



    def getPage(self,code):

        url = self.URL 

        request = urllib2.Request(url)

        response = urllib2.urlopen(request)

        return response.read().decode('utf-8')



    def getContents(self,code):

        page = self.getPage(code)

        pattern = re.compile('none;">(.*?)&nbsp;</a>',re.S)

        result = re.findall(pattern,page)

        for results in result:

         y = open("results.txt","a") 

         y.writelines(results+'\n')

         y.close()





Badiuspider = Spider()

spider.getContents(1)



print "Everything is OK"

