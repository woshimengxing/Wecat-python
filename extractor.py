#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests as req
import re


from urllib import parse
from urllib.request import urlretrieve

DBUG   = 0

reBODY =re.compile( r'<body.*?>([\s\S]*?)<\/body>', re.I)
reCOMM = r'<!--.*?-->'
reTRIM = r'<{0}.*?>([\s\S]*?)<\/{0}>'
reTAG  = r'<[\s\S]*?>|[ \t\r\f\v]'
reUri  = r'?<=http[s]://)[.\w-]*(:\d{,8})?((?=/)|(?!/)'

reIMG  = re.compile(r'<img[\s\S]*?src=[\'|"]([\s\S]*?)[\'|"][\s\S]*?>')
reIMG22  = r'<img[\s\S]*?src=[\'|"]([\s\S]*?)[\'|"][\s\S]*?>'

class Extractor():
    def __init__(self, url = "", blockSize=3, timeout=5, image=False):
        self.url       = url
        self.blockSize = blockSize
        self.timeout   = timeout
        self.saveImage = image
        self.rawPage   = ""
        self.ctexts    = []
        self.cblocks   = []
    def getRawPage(self):
        try:
            resp = req.get(self.url, timeout=self.timeout)
        except Exception as e:
            raise e

        if DBUG: print(resp.encoding)

        resp.encoding = "UTF-8"

        return resp.status_code, resp.text

    def processTags(self):
        self.body = re.sub(reCOMM, "", self.body)
        self.body = re.sub(reTRIM.format("script"), "" ,re.sub(reTRIM.format("style"), "", self.body))
        # self.body = re.sub(r"[\n]+","\n", re.sub(reTAG, "", self.body))
        self.body = re.sub(reTAG, "", self.body)

    def processBlocks(self):
        self.ctexts   = self.body.split("\n")
        self.textLens = [len(text) for text in self.ctexts]

        self.cblocks  = [0]*(len(self.ctexts) - self.blockSize - 1)
        lines = len(self.ctexts)
        for i in range(self.blockSize):
            self.cblocks = list(map(lambda x,y: x+y, self.textLens[i : lines-1-self.blockSize+i], self.cblocks))

        maxTextLen = max(self.cblocks)

        if DBUG: print(maxTextLen)

        self.start = self.end = self.cblocks.index(maxTextLen)
        while self.start > 0 and self.cblocks[self.start] > min(self.textLens):
            self.start -= 1
        #while self.end < lines - self.blockSize and self.cblocks[self.end] > min(self.textLens):
        #    self.end += 1
        while self.end < lines:
            self.end += 1
        return "\n".join(self.ctexts[self.start:self.end])

    def processImages(self):
        #try:
          imgs = re.findall(reIMG22,self.body)
          for img in imgs:
            if(('http' in img) == False):
               img= 'http:'+img
            urlretrieve(img,'E:\\BaiduArrange-master\\img\\'+self.getimg_name(img))
        #except:
          #print("img erreo")

    def getContext(self):
        code, self.rawPage = self.getRawPage()
        self.body = re.findall(reBODY, self.rawPage)[0]

        if DBUG: print(code, self.rawPage)

        if self.saveImage:
            self.processImages()
        self.processTags()
        return self.processBlocks()
        # print(len(self.body.strip("\n")))

    def getimg_name(self,img_name):
        
        img_names = img_name.split('/')
        #print(img_names)
        return img_names[len(img_names)-1]


    def geta_url_sougou(a_url):
        url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', req.get(a_url).text)
        return url[0]
    

    def get_url(a_url,type):
        url = ""
        if (type == 'baidu'):
            url = req.get(a_url).url
        elif (type == 'sougou'):
            url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', req.get(a_url).text)[0]

        return parse.urlparse(url).netloc

if __name__ == '__main__':
    ext = Extractor(url="http://wdg.cnshuomi.cn/",blockSize=5, image=False)
    print(ext.getContext())
